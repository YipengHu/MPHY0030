% script_icp

%% read the data
px = csvread('../data/points_x.csv');
py = csvread('../data/points_y.csv');


objICP = IterativeClosestPoint(px,py);
objICP = objICP.register;

py_transformed = objICP.applyTransform(py,objICP.Transform);


%% plot points
% figure, plot3(px(:,1),px(:,2),px(:,3),'r.');
% hold on; plot3(py(:,1),py(:,2),py(:,3),'b.');
% hold on; plot3(py_transformed(:,1),py_transformed(:,2),py_transformed(:,3),'g.');
% axis equal

% plot surfaces
trix = csvread('../data/tris_x.csv');
triy = csvread('../data/tris_y.csv');

figure, axis equal, hold on;
h1 = patch('vertices',px,'faces',trix, ...
    'facecolor','r','edgecolor','r','edgealpha',.2,'facealpha',.2);
h2 = patch('vertices',py,'faces',triy, ...
    'facecolor','b','edgecolor','b','edgealpha',.2,'facealpha',.2);
h3 = patch('vertices',py_transformed,'faces',triy, ...
    'facecolor','g','edgecolor','g','edgealpha',.2,'facealpha',.2);
view(3); light; lighting phong;
legend([h1,h2,h3],'Fixed','Moving','Transformed')