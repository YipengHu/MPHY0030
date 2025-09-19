# MPHY0030: Programming Foundations for Medical Image Analysis 
UCL Module | [MPBE](https://www.ucl.ac.uk/medical-physics-biomedical-engineering/) | [UCL Moodle Page](https://moodle.ucl.ac.uk/)
>Term 1 (Autumn)  


Yipeng Hu       | yipeng.hu@ucl.ac.uk        | Lead   
Shaheer U Saeed | shaheer.saeed.17@ucl.ac.uk | lecturer  
Yunzhe Li       | yunzhe.li.22@ucl.ac.uk     | tutor  
Bilal Sidiqi    | bilal.sidiqi.21@ucl.ac.uk  | tutor  
Maruf Talukdar  | zcapmta@ucl.ac.uk          | tutor  


## 1. Development environment 
There is no requirement, in tutorials or assessed coursework, for what the development environment or tools that need to be used. However, technical support from this module is available for the setups detailed in the following documents, under `docs` folder.
- [Supported development environment for Python](./docs/dev_env_python.md)

### Python environment
The tutorials require a few dependencies, numpy, scipy, matplotlib. Individual tutorials may also require other libraries which will be specified in the readme.md in individual tutorial folders (see links below).

Creating and using a virtual environment is recommended when setting up the Python development environment. For example:
```bash
python3 -m venv mphy0030
source mphy0030/bin/activate
python -m pip install --upgrade pip
pip install numpy scipy matplotlib
```
When you are finished, you can deactivate the environment or before switching/creating a new one:
```bash
deactivate
```

## 2. Python refresher course
This mini-course has two parts, Python programming and scientific computing, by Shaheer Saeed. Materials can also be found in the [`tutorials`](./tutorials/) folder.


## 3. Tutorials
These are the tutorials under the [`tutorials`](./tutorials/) folder using Python, with optionally assessed questions.

>MATLAB is a proprietary multi-paradigm programming language and numerical computing environment developed by MathWorks. Some tutorials are also additionally with MATLAB code for those who have relevant experience. 


### Image filtering 3d
Efficient high-dimensional image filtering  
[Tutorial][image_filtering_3d]

[image_filtering_3d]: ./tutorials/image_filtering_3d/readme.md

### Maximum intensity projection 
Inverting computerised tomography to obtain x-ray images  
[Tutorial][maximum_intensity_projection]

[maximum_intensity_projection]: ./tutorials/maximum_intensity_projection/readme.md

### Iterative closest point 
A point set registration algorithm, iterative closest point (ICP)  
[Tutorial][iterative_closest_point]

[iterative_closest_point]: ./tutorials/iterative_closest_point/readme.md

### Augmented reality on medical images
Display graphics overlaid with 3d medical imges  
[Tutorial][augmented_reality]

[augmented_reality]: ./tutorials/augmented_reality/readme.md


## *Legacy materials
The [`legacy`](./tutorials/legacy/) folder contains several tutorials used in previous years for expanding knowledge of the students who are interested in.
