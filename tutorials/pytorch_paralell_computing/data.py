import torch
import os
import torchvision.transforms.functional as tf
from torch.utils.data import Dataset
from PIL import Image
from glob import glob


class BrainTumorSegData(Dataset):
    def __init__(self, phase):
        assert phase in ['train', 'val', 'test']
        self.phase = phase  # train/val/test
        self.image_root = './data/'
        self.datalist = glob(os.path.join(self.image_root, phase, '*_mask.tif'))
        
    def __getitem__(self, index):
        msk_path = self.datalist[index]
        img_path = msk_path.replace('_mask', '')
        img_id = os.path.basename(img_path).replace('.tif', '')
        
        img, msk = Image.open(img_path), Image.open(msk_path)
        img, msk = tf.to_tensor(img), tf.to_tensor(msk) 

        return img, msk, img_id

    def __len__(self):
        return len(self.datalist)
