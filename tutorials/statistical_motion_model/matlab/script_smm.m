%  &PlotMVData



%% load data
load('data_shapes');
training_data = cell2mat( ...
    cellfun(@(x) reshape(x,[],1),nodes_training,'UniformOutput',false) );

L = 20;
[PCs,lambda] = PCA_eig(training_data);
PCs = PCs(:,1:L); lambda=lambda(1:L);
mShape = mean(training_data,2);

b = -sqrt(lambda)*2;
x = PCA_reconstruction(mShape,b,PCs);
nodes1 = reshape(x,[],3);

b = sqrt(lambda)*2;
x = PCA_reconstruction(mShape,b,PCs);
nodes2 = reshape(x,[],3);



%% plot points
figure
plot3(nodes1(:,1),nodes1(:,2),nodes1(:,3),'.');
axis equal

figure
plot3(nodes2(:,1),nodes2(:,2),nodes2(:,3),'.');
axis equal


%% plot surface
figure
patch('faces',tris,'vertices',nodes1,'facecolor','none');
axis equal

figure
patch('faces',tris,'vertices',nodes2,'facecolor','none');
axis equal


%% animation

nodes0 = reshape(PCA_reconstruction(mShape,zeros(L,1),PCs),[],3);

hf = figure('position',[1,1,800,600],'color',[0,0,0]); 
ha = axes('parent',hf,'color',[0,0,0]);hold on;
hp = patch('parent',ha,'faces',tris,'vertices',nodes0);
set(hp,'facecolor','magenta','facealpha',1,'edgecolor','none');
view(0,-85); % view(-95,0);   
axis equal; zoom(1);
camlight('headlight'); lighting phong; 
htitle = title('b1 = ','color','w','fontsize',25);

numf = 100;

bnum = 5;
% 
clear MOV; fr = 1;  % MOV(fr) = getframe(hf); fr=fr+1;
b = zeros(L,1);
for  i = 1:numf
   b(bnum) = -sqrt(lambda(bnum))*3 + sqrt(lambda(bnum))*6*i / numf;
   nodes = reshape(PCA_reconstruction(mShape,b,PCs),[],3);
   set(hp,'vertices',nodes);
   set(htitle,'string',sprintf('b%d = %0.4f',bnum,b(bnum)))
   MOV(fr) = getframe(hf); fr=fr+1;
end

WriteMovie(sprintf('AniShapeModel_b%d',bnum),MOV);




