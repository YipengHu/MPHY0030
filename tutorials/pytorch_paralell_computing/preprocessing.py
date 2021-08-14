import os
from glob import glob
from PIL import Image
import numpy as np
from shutil import copyfile


dest_folder = './data'
os.mkdir(dest_folder)

def has_tumor(img_path):
    img = Image.open(img_path)
    img_arr = np.array(img)
    return img_arr.max() > 0
    
os.system('unzip ./raw_data/archive.zip -d ./raw_data')

image_folders = [i for i in glob('./raw_data/kaggle_3m/*') if os.path.isdir(i)]

train_folders = image_folders[:90]
val_folders = image_folders[90:100]
test_folders = image_folders[100:]

phases = ['train', 'val', 'test']
for idx, f in enumerate([train_folders, val_folders, test_folders]):
    phase_folder = os.path.join(dest_folder, phases[idx])
    os.mkdir(phase_folder)
    for imf in f:
        print(f'processing {imf}')
        masks = [i for i in glob(os.path.join(imf, '*_mask.tif')) if has_tumor(i)]
        imgs = [i.replace('_mask', '') for i in masks]
        [copyfile(i, os.path.join(phase_folder, os.path.basename(i))) for i in masks]
        [copyfile(i, os.path.join(phase_folder, os.path.basename(i))) for i in imgs]
