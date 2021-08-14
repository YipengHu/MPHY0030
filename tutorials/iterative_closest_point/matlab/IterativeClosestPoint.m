% class IterativeClosestPoint

classdef IterativeClosestPoint
    
    properties (SetAccess=private, GetAccess=public)
        PointSetX
        PointSetY
        Transform
        DTriX  % Delaunay triangulation from point set X
    end
    
    properties (SetAccess=public, GetAccess=public)
        MaxIter
        TolD
    end
    
    properties (SetAccess=private, GetAccess=public, Dependent=true)
        NumX, NumY
    end
    
    
    methods       
        % constructor
        function obj = IterativeClosestPoint(px, py)
            obj.PointSetX = px;
            obj.PointSetY = py;
            if any([size(px,2),size(py,2)]~=3)
                error('Only 3-dimensional points are accepted.')
            end
            % initialise identity transformation
            obj.Transform = [eye(3);zeros(1,3)];  % [rotation; translation]
            % default optimisation parameters
            obj.MaxIter = 1e3;
            obj.TolD = 1e-5;
            obj.DTriX = delaunay(px);  % precompute for searching closest points
        end
        
        % set dependent properties
        function  nx = get.NumX(obj)
            nx = size(obj.PointSetX,1);
        end
        function  ny = get.NumY(obj)
            ny = size(obj.PointSetY,1);
        end
        
        function obj = register(obj)
            % compute initial t as the difference between centroids
            obj.Transform(4,:) = mean(obj.PointSetX,1)-mean(obj.PointSetY,1);
            tmpDist = inf;
            for ii = 1:obj.MaxIter
                % apply current transformation
                tmpPointSetY = obj.applyTransform(obj.PointSetY, obj.Transform);
                % find the closest point
                idx = dsearchn(tmpPointSetY,obj.DTriX,obj.PointSetX);
                % compute the transformation
                [obj.Transform,Dist] = obj.computeTransform(obj.PointSetX(idx,:),obj.PointSetY);
                fprintf('Iter=%d, d=%f.\n',ii,Dist);
                if abs(Dist-tmpDist)<obj.TolD
                    fprintf('Tolerance in residual distance change (%f) reached.\n', obj.TolD);
                    break
                else
                    tmpDist = Dist;
                end
            end
            
        end
    end
    
    
    methods (Static)
        function tY = applyTransform(Y,tform)
            tY = Y*tform(1:3,:) + ones(size(Y,1),1)*tform(4,:);
        end
        
        function  [tform,d] = computeTransform(X,Y,correct_reflect)
            %The absolute orientation solution
            % usage:
            %      [tform,d] = computeTransform(X,Y);
            %
            % input:
            %     X      - np-by-dim points
            %     Y      - np-by-dim points
            %     correct_reflect   - correct the reflection caused by SVD
            % output:
            %     tform - [rotation matrix; translation vector]
            %     d - minimised distance
            % such that: |X - Y*tform(1:3,;)+repmat(tform(4,:),np,1)|^2 is minimised.
            
            if  nargin<4, correct_reflect=true; end
            
            %%% find the centroids
            xmean = mean(X);
            ymean = mean(Y);
            
            %%% centred data
            np = size(X,1);
            nX = X-repmat(xmean,np,1);
            nY = Y-repmat(ymean,np,1);
            
            %%% SVD calculating rotation, R
            [U,S,V] = svd(nX'*nY);
            if  correct_reflect
                R = V*diag([1,1,det(V*U')])*U';
            else
                R = V*U';
            end
            
            %%% translation
            tform = [R; xmean-ymean*R];
            
            %%% configurations' distance
            % d = sqrt(trace(nX'*nX)+trace(nY'*nY)-2*trace(S));
            d = sqrt(mean(sum((Y*R+ones(np,1)*tform(4,:)-X).^2,2)));
            
        end
        
    end
    
end
    