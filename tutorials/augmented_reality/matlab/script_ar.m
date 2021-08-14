% script to display images with segmented organs


%% read in image and masks
image = niftiread('../data/image.nii.gz');
masks = niftiread('../data/masks.nii.gz');
info = niftiinfo('../data/image.nii.gz');
% niftiwrite(int16(image),'image',info,'Compressed',true);
% niftiwrite(uint8(masks),'masks',info,'Compressed',true);



[sy,sx,sz] = size(image);  % volum size
% coordinates in each dimension in mm 
cx = (0.5:sx-0.5) * info.PixelDimensions(2);
cy = (0.5:sy-0.5) * info.PixelDimensions(1);
cz = (0.5:sz-0.5) * info.PixelDimensions(3);


%% extract surfaces from the masks
idx_masks = [3, 6, 8];  % change this line to display other structures

fv = {};
for ii = 1:length(idx_masks)
    % extract iso-surface mesh from the smoothed volume
    fv_tmp = isosurface(cx,cy,cz,smooth3(masks(:,:,:,idx_masks(ii))),0.5);
    % reduce surface triangle number per the size of the structure
    fv_tmp = reducepatch(fv_tmp, nnz(masks(:,:,:,idx_masks(ii)))^(2/3));
    fv{ii} = fv_tmp;
end


%% set the slice(s) to display in each dimension in mm
slx = [80] * info.PixelDimensions(2);
sly = [] * info.PixelDimensions(1);
slz = [150] * info.PixelDimensions(3);


%% display
colors = parula(length(fv));
figure
for ii = 1:length(fv)
    patch(fv{ii},'facealpha',0.2,'facecolor',colors(ii,:),'edgealpha',0.5,'edgecolor',colors(ii,:))
end
hold on;
hslice = slice(cx,cy,cz,single(image),slx,sly,slz);
set(hslice,'edgecolor','none')
colormap('gray')
axis equal tight
view(-200,25)
