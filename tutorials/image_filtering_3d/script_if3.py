# script for separable convolution for higher dimensional image

import numpy as np
import SimpleITK as sitk 

# read in image
itk_image = sitk.ReadImage("data/cardiac_t2.nii.gz", imageIO="NiftiImageIO")
image = sitk.GetArrayFromImage(itk_image).astype(np.float32)

# generate a 1-d Gaussian kernel 
sigma = 3
tail = int(sigma*3)
kernel = np.exp([-0.5*x**2/sigma**2 for x in range(-tail, tail+1)]).astype(np.float32)
kernel = kernel / np.sum(kernel)

# separable convolution in each dimension
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i,j,:] = np.convolve(image[i,j,:],kernel,'same')

for i in range(image.shape[0]):
    for k in range(image.shape[2]):
        image[i,:,k] = np.convolve(image[i,:,k],kernel,'same')

for j in range(image.shape[1]):
    for k in range(image.shape[2]):
        image[:,j,k] = np.convolve(image[:,j,k],kernel,'same')

# save the filtred image
itk_image_f = sitk.GetImageFromArray(image.astype(np.uint8))
itk_image_f.CopyInformation(itk_image)  # get information from the original image header
filename = "data/cardiac_t2_python.nii.gz"
sitk.WriteImage(itk_image_f, filename, imageIO="NiftiImageIO")

print('Filtered image is saved %s.' % filename)
