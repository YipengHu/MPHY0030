% script for separable convolution for higher dimensional image

%% read image
image = single(niftiread('../data/cardiac_t2.nii.gz'));

%% generate a 1-d Gaussian kernel
sigma = 3;
tail = round(sigma*3);
kernel = exp((-tail:tail).^2.*(-.5)/(sigma^2));
kernel = single(kernel / sum(kernel));

%% separable convolution in each dimension
image = convn(image,reshape(kernel,1,1,[]),'same');
image = convn(image,reshape(kernel,1,[],1),'same');
image = convn(image,reshape(kernel,[],1,1),'same');

%% save the filtered image with original file header
filename = '../data/cardiac_t2_matlab';
niftiwrite(uint8(image),filename,niftiinfo('../data/cardiac_t2.nii.gz'),'Compressed',true)
fprintf('Filtered image is saved %s.\n', filename)