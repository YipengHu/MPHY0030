import torch
import torchvision
import logging
import torch.optim as optim
from config import args
from data import BrainTumorSegData
from torch.utils.data import DataLoader
from torch.nn import functional
from loss import DiceLoss, binary_dice
from networks import UNet
import os
import utils

'''
*** means key steps, otherwise optional.
'''

# Print the params #
for key, item in args.__dict__.items():
    print(f'{key} : {item}') 

#*** GPU setting ***#
os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
torch.backends.cudnn.benchmark = True


# Set a model #
if args.model=='unet':
    model = UNet(in_channels=3, out_channels=1)
elif args.model=='deeplabv3_resnet50':
    model = torchvision.models.segmentation.deeplabv3_resnet50(num_classes=2)
elif args.model=='fcn_resnet50':
     model = torchvision.models.segmentation.fcn_resnet50(num_classes=2)
else:
    raise ValueError("wrong model")

#*** GPU setting ***#
model.cuda()

# Get outputs from a model #
def get_output(args, model, x):
    if args.model=='unet':
        out = model(x)
    elif args.model=='deeplabv3_resnet50':
        out = model(x)['out'][:, 1:2]
        out = functional.sigmoid(out)
    elif args.model=='fcn_resnet50':
        out = model(x)['out'][:, 1:2]
        out = functional.sigmoid(out)
    else:
        pass
    return out

#*** Data Loaders ***# 
trainset = BrainTumorSegData(phase='train')
trainloader = DataLoader(trainset, batch_size=args.batch_size, shuffle=True, num_workers=4)
valset = BrainTumorSegData(phase='val')
valloader = DataLoader(valset, batch_size=1, shuffle=False, num_workers=4)
testset = BrainTumorSegData(phase='test')
testloader = DataLoader(testset, batch_size=1, shuffle=False, num_workers=4)

#*** Set optimizer and loss function ***#
optimizer = optim.Adam(model.parameters(), lr=args.lr)
dice_loss = DiceLoss()


#*** Train and validation loop ***#
best = 0
for epoch in range(args.epochs):
    model.train()
    for step, (img, msk, img_id) in enumerate(trainloader):
        img, msk = img.cuda(), msk.cuda()
        optimizer.zero_grad()
        out = get_output(args, model, img)
        loss = dice_loss(out, msk)
        loss.backward()
        optimizer.step()
        print(f'epoch {epoch}, {step*args.batch_size}/{len(trainset)}, loss={loss:.3f}')

    model.eval()
    with torch.no_grad():
        print('in validation...')
        losses = []
        for idx, (img, msk, img_id) in enumerate(valloader):
            img, msk = img.cuda(), msk.cuda()
            out = get_output(args, model, img)
            dsc = binary_dice(msk, out)
            losses.append(dsc)
        avg = torch.mean(torch.tensor(losses)).cpu().numpy()
        std = torch.std(torch.tensor(losses)).cpu().numpy()
        print(avg, std)
        if avg > best:
            best = avg
            best_epoch = epoch
            best_model_path = utils.save_model(model, args, model_name='best.pth')
        if (epoch+1)%args.save_period==0:
            model_path = utils.save_model(model, args, model_name=f'epoch-{epoch}.pth')


#*** Test  ***#
with torch.no_grad():
    print('final test...')
    print(f'inference with best model from epoch {best_epoch}')
    model = torch.load(best_model_path)
    model = model.cuda()
    losses = []
    for idx, (img, msk, img_id) in enumerate(testloader):
        img, msk = img.cuda(), msk.cuda()
        out = get_output(args, model, img)
        dsc = binary_dice(msk, out)
        losses.append(dsc)
        print(idx, img_id[0], f'dsc:{dsc:.3f}')

        save_path = os.path.join('./vis', args.exp_name, str(best_epoch))
        os.makedirs(save_path, exist_ok=True)
        utils.save_img(out, img, msk, save_path, img_id)
    avg = torch.mean(torch.tensor(losses)).cpu().numpy()
    std = torch.std(torch.tensor(losses)).cpu().numpy()
    print(f'DICE SCORE, Mean: {avg}, Std:{std}')
