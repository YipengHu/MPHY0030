import numpy as np
from PIL import Image 


# read an image
IMG_FILE = '../data/mri_prostate.dat'
img0 = np.genfromtxt(IMG_FILE,delimiter=',',dtype='uint8')
M, N = img0.shape

# build a Gaussian kernel
s = 0.01  # scale 
x, y = np.linspace(-M/2,M/2,M), np.linspace(-N/2,N/2,N)
grid_x, grid_y = np.meshgrid(x, y)
kernel = np.exp(-(grid_x**2+grid_y**2)*s)
kernel = kernel / kernel.sum()  # normalisation

# filtering
img0_fft = np.fft.fft2(img0) # FFT
img0_fft = np.fft.fftshift(img0_fft) # zero-freq. locations
img1_fft = img0_fft * kernel # multiplication in frequency domain
img1 = np.fft.ifft2(img1_fft) # inverse FFT
img1 = np.abs(img1) # real part

# save to files
img1 = (img1-img1.min()) / (img1.max()-img1.min()) *255 # to uint8
Image.fromarray(img1.astype('uint8')).save('fft_s1e-2.png')
