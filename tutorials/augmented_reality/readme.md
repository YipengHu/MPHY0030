# Augmented reality 


## Python
Additional library SimpleITK and scikit-image are required in addition to those set up in the `mphy0030` environment.
```bash
conda activate mphy0030
pip install simpleitk scikit-image numpy-stl
```

Then you can run the script.
```bash 
cd python  
python script_ar.py  
```

Then use any medical image viewer to load the image and the surface model data. The 3D slicer displays it as below.  

![augmented_ct](./python/slicer_display.jpg)


## MATLAB
```bash
cd matlab  
matlab -nodesktop -r script_ar  
```
