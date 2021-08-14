function  [U,sigma,B] = PCA_eig(X,useGram)

%[U,sigma,B] = PCA_eig(X);
% Principal component analysis (PCA) on X using eigen-decomposition.
%
%INPUTS: 
%     X:     m-by-n data, m: dimensions, n: observations
%
%OUTPUTS:
%     U:     columns are principal components.
%     sigma: corresponding variances for each mode.
%     B:     scores or signal.
% 
%Function Dependency: None
%
% see also PCA_rec PCA_svd 

% Yipeng Hu, CMIC, UCL, 2007-2012

% M dimensions - N observations
[M,N] = size(X);

% always work in lower dimensionality if useGram not provided
if  nargin<2, if(M>N), useGram=true; else useGram=false; end; end

% subtract mean
X = X - mean(X,2)*ones(1,N);

if  ~useGram,
    % covariance matrix
    C = 1/(N-1)*(X*X');
    % compute eigenvectors and eigenvalues
    [U,sigma] = eig(C);
    sigma = diag(sigma);
else
    % decomposing the Gram matrix
    [V,sigma] = eig(1/(N-1)*(X'*X));
    sigma = diag(sigma);
    U = X*V * diag(1./(sqrt((N-1)*sigma)));  % normalisation so that norm(U(:,i))=1;
end

% sorting in decreasing order    
[sigma,ix] = sort(sigma,'descend');
U = U(:,ix);

% compute scores
if(nargout>2), B = U'*X; end


