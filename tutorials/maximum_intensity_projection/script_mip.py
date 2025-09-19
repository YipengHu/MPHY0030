# script to compute a digitally reconstructed radiography (DRR) using
# maximum intensity projection (MIP)

from scipy.io import loadmat
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interpn

## load a 3D CT volume data
# 1-j -> anterior->posterior
# 0-i -> right->left (drr_x)
# 2-k -> superior->caudal (drr_y)
mat_data = loadmat('../data/test_lung_ct.mat')
vol = mat_data['vol'].astype('float16')  # plt.imshow(vol[:100,:,100])
voxdims = mat_data['voxdims'][0]

# - using x-ray source coordinates, i.e. x0=[0,0,0], for spherical coordinates
# - assuming 100 cm distance between source to detector
# - assuming a drr_size cm^2 detector with a resolution of drr_voxdims under the body
d_x2d = 1000
drr_size = (200,120)
drr_voxdims = (0.8,0.8)


## centring the volume coordinates
vol_i = np.linspace(-vol.shape[0]/2+0.5,vol.shape[0]/2-0.5,vol.shape[0])*voxdims[0]
vol_j = d_x2d - np.linspace(vol.shape[1]-0.5,0.5,vol.shape[1])*voxdims[1]
vol_k = np.linspace(-vol.shape[2]/2+0.5,vol.shape[2]/2-0.5,vol.shape[2])*voxdims[2]


## detector:
[drr_i, drr_j] = np.meshgrid(
    np.linspace(-drr_size[0]/2+0.5,drr_size[0]/2-0.5,drr_size[0])*drr_voxdims[0],
    np.linspace(-drr_size[1]/2+0.5,drr_size[1]/2-0.5,drr_size[1])*drr_voxdims[1],
    indexing='ij')


# get the range of r
vol_ds = np.sqrt(sum([x**2 for x in np.meshgrid(vol_i,vol_j,vol_k,indexing='ij')]))
drr_ds = np.sqrt(drr_i**2+drr_j**2+d_x2d**2)
r_max = max([vol_ds.max(),drr_ds.max()])
r_min = min([vol_ds.min(),drr_ds.min()])
n_samples = int(np.ceil(1.5*(r_max-r_min)))
# get spehrical coordinates
az = np.arctan2(drr_i,drr_j)[...,np.newaxis]
el = np.arctan2(d_x2d,np.sqrt(drr_i**2 + drr_j**2))[...,np.newaxis]
r = np.reshape(np.linspace(r_min,r_max,n_samples),(1,1,n_samples))
# convert back to cartesian
sample_z = r * np.cos(el) * np.cos(az)
sample_y = r * np.cos(el) * np.sin(az)
sample_x = r * np.sin(el)


## interpolation get sample values
samples = interpn(
                (vol_i,vol_j,vol_k), 
                vol, 
                np.stack([sample_y,sample_x,sample_z],axis=3),
                method='linear', bounds_error=False, fill_value=0.0,
                )

# compute DDR
DRR = np.amax(samples,axis=2)


## display
# plt.imshow(DRR,cmap='gray')
# plt.show()

## save to a file
plt.imsave('../data/drr_python.png',DRR,cmap='gray')
