# Statistical shape modelling in image-guided intervention

## Introduction
Statistical shape models (SSM), especially those based on principal component analysis (an easy-to-follow tutorial on PCA can be found [here][Shlens]), have been (re)introduced in medical imaging since about a quater of century ago. Among the first applications, SSMs were applied to modelling human hands in pictures and shapes of the heart in ultrasound images (see an [example][Cootes et al]). Later, variants of SSM have found many applications in medical image computing and computer-assisted interventions, for the later of which, ranging from cadiological motion analysis, intraoperative liver segmentation to multimodality neuralimaging fusion. [A review paper for SSM research][Heimann et al] gives an overview of these methods. 


## Workshop
This workshop uses a UCL-developed [clinical application][Hu et al] in minimally-invasive prostate cancer intervention as an example. The goals of this hands-on-workshop are as follows,
1) to demonstrate an organ motion model used in real-world application; 
2) to implement the powerful PCA in python;
3) to test a simplified data fusion algorithm and to visualise the results.


[Heimann et al]: http://ww.vavlab.ee.boun.edu.tr/courses/574/material/Statistical%20Methods/heimann_StatisticalShapeModels.pdf
[Cootes et al]: http://homes.di.unimi.it/~casiraghi/PAGINAINTERNETELABIMGS/ASM/ASM_95.pdf
[Shlens]: https://arxiv.org/pdf/1404.1100.pdf
[Hu et al]: http://www.medicalimageanalysisjournal.com/article/S1361-8415(10)00129-5/pdf


## Software
By now, it is assumed that everyone is familier with jupyter notebook and python. The python libraries (NumPy and matplotlib) needed for this workshop are also included in Anaconda, otherwise for power users, are easy to install along the way. Run the following sections in order.


## [01-Data][data]
Have a look at the data, representing surfaces of deformed prostate glands simulated by finite-element modelling, basic display for exploring the application and understand the intraoperative data fusion problem.

[data]: 01-data.ipynb


## [02-PCA][pca]
Details in implementing the PCA method that underpins SSM.

[pca]: 02-pca.ipynb


## [03-Fusion][fusion]
Demonstration of an simplified application to use the SSM developed in the previous section, to calculate the data fusion errors and to deal with noisy and missing data.

[fusion]: 03-fusion.ipynb
