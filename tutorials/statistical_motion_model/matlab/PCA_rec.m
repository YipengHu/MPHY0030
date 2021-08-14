function  [b,y_new,r] = PCA_rec(X,y,L)

%[b,y_new,r] = PCA_rec(X,y,L);
% Reconstruct data y 
%
%INPUTS: 
%     X:     m-by-n data, m: dimensions, n: observations
%     y:     m-by-nn data, m: dimensions, nn: number of tests
%
%OUTPUTS:
%     b:     scores or signal.
%     y_new: reconstructed y.
%     r:     residuals.
% 
%Function Dependency: PCA_eig
%
% see also PCA_eig 

% Yipeng Hu, CMIC, UCL, 2007-2012




%% perform PCA
U = PCA_eig(X);
U = U(:,1:L);
mx = mean(X,2);

% compute new b
N = size(y,2);
b = U'*(y-mx*ones(1,N));

% reconstruct y_new
y_new = mx*ones(1,N) + U*b;

% residuals
r = y_new-y;




