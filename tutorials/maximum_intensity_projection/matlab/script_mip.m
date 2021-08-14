% script to compute a digitally reconstructed radiography (DRR) using
% maximum intensity projection (MIP)

%% load a 3D CT volume
load('../data/test_lung_ct.mat')

%% get the DRR position
% x -> anterior->posterior
% y -> right->left (drr_x)
% z -> superior->caudal (drr_y)

% - using x-ray source coordinates, i.e. x0=[0,0,0], for spherical coordinates
% - assuming 100 cm distance between source to detector
% - assuming a drr_size cm^2 detector with a resolution of drr_voxdims under the body
d_x2d = 1000;
drr_size = [200,120];  % [y,x] in DRR
drr_voxdims = [1,1];

% centring the volume coordinates
vol_size = size(vol);
[vol_x, vol_y, vol_z] = meshgrid(d_x2d - (vol_size(2)-0.5:-1:0.5)*voxdims(2), ...
                                (-vol_size(1)/2+0.5:vol_size(1)/2-0.5)*voxdims(1), ...
                                (-vol_size(3)/2+0.5:vol_size(3)/2-0.5)*voxdims(3)); % volume on the detector
vol_ds = sqrt(vol_x.^2+vol_y.^2+vol_z.^2);

% detector:
[drr_x,drr_y] = meshgrid((-drr_size(2)/2+0.5:drr_size(2)/2-0.5) * drr_voxdims(2), ...
                        (-drr_size(1)/2+0.5:drr_size(1)/2-0.5) * drr_voxdims(1));
drr_ds = sqrt(drr_x.^2 + drr_y.^2 + d_x2d^2);
% get the range of r
r_max = max([vol_ds(:);drr_ds(:)]);
r_min = min([vol_ds(:);drr_ds(:)]);
n_samples = ceil(1.5*(r_max-r_min));
% get spehrical coordinates, [az,el,r]
[az,el] = cart2sph(drr_x,drr_y,d_x2d);
az = repmat(az,[1,1,n_samples]);
el = repmat(el,[1,1,n_samples]); 
r = repmat(reshape(linspace(r_min,r_max,n_samples),1,1,n_samples),[drr_size(1),drr_size(2),1]);
% convert back to cartesian
[sample_z, sample_y, sample_x] = sph2cart(az,el,r);
% figure, plot3(sample_x(:),sample_y(:),sample_z(:),'.'); axis equal

% interpolation get sample values
samples = interp3(vol_x,vol_y,vol_z,single(vol),sample_x,sample_y,sample_z,'*linear',0);

% compute DDR
DRR = max(samples,[],3);
%% display
figure, imshow(DRR,[])
