# script for displaying structures on medical images
import numpy as np
import SimpleITK as sitk 
from skimage.measure import marching_cubes
from stl import mesh

# image_id = sitk.ReadImage("../data/image.nii.gz", imageIO="NiftiImageIO")
# image = sitk.GetArrayFromImage(image_id)
# vox_dims = image_id.GetSpacing()
mask_id = sitk.ReadImage("data/masks.nii.gz", imageIO="NiftiImageIO")
masks = sitk.GetArrayFromImage(mask_id)
vox_dims = mask_id.GetSpacing()

"""Note
It may not be trivial to display high dimensional image volume and segmented anatomical structures.
In this tutorial, these extracted surface models are written in STL files that can be read by many medical image viewers, such as 3D Slicer (www.slicer.org).
"""

# extract surfaces from the masks
# strictly speaking, this files need to be take into account the full transformation to scanner coordinates - which is an identity matrix in this case.
for ii in range(masks.shape[0]):
    # extract an iso-surface coarser mesh from the volume
    vertices, faces, _, _ = marching_cubes(masks[ii,...],spacing=vox_dims[0:3],step_size=2)
    vertices = np.stack([vertices[:,2],vertices[:,1],vertices[:,0]],axis=1)
    roi = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            roi.vectors[i][j] = vertices[f[j],:]
    roi.save('../data/roi%02d.stl' % ii)
