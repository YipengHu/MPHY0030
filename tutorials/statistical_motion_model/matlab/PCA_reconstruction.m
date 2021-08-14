function  [y_new,r] = PCA_reconstruction(mx,b,U)


% compute new b
N = size(b,2);

% reconstruct y_new
y_new = mx*ones(1,N) + U*b;

% residuals
if  nargout>1, r = y_new-y; end




