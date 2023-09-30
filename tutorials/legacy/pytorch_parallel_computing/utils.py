import torch
import os
import numpy as np
import matplotlib.pyplot as plt

def save_model(model, args, model_name):

    exp_name = args.exp_name
    os.makedirs(os.path.join(args.logdir, exp_name), exist_ok=True)
    model_path = os.path.join(args.logdir, exp_name, model_name)
    print(f'saving model to {model_path}')
    torch.save(model, model_path)
    return model_path

def save_img(out, img, msk, save_path, img_id):
    out = out.cpu().numpy()[0, 0, :, :]
    out = np.concatenate([out[..., None]]*3, axis=2)
    
    img = img.cpu().numpy()[0, :, :, :]
    img = np.transpose(img, (1, 2, 0))

    msk = msk.cpu().numpy()[0, 0, :, :]
    msk = np.concatenate([msk[..., None]]*3, axis=2)
    cc = np.concatenate([img, msk, out], axis=1)
    plt.imsave(os.path.join(save_path, img_id[0] + '.png'), cc)