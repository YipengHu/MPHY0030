%  &Anim_ShapeData

load('data_shapes');

% original plotting
hf = figure('position',[1,1,800,600],'color',[0,0,0]); 
ha = axes('parent',hf,'color',[0,0,0]); hold on;
hp = patch('parent',ha,'faces',tris,'vertices',nodes_training{1});
set(hp,'facecolor','magenta','edgecolor','magenta');
% set(hp,'facecolor','none','linestyle','.');
view(0,-85);  view(-95,0); 
axis equal; axis tight; axis manual; 
xyzlim = get(ha,{'xlim','ylim','zlim'});
xyzlim = cellfun(@(x) (x-mean(x))*1.5+mean(x), xyzlim,'UniformOutput',false);
set(ha,{'xlim','ylim','zlim'},xyzlim);
camlight('headlight'); lighting phong; 

clear MOV; fr = 1;  % MOV(fr) = getframe(hf); fr=fr+1;
n = 50;
for j = 1:n,
   set(hp,'vertices',nodes_training{j});
   drawnow;
   MOV(fr) = getframe(hf); fr=fr+1;
end


WriteMovie('ShapeData_transverse',MOV);

WriteMovie('ShapeData_profile',MOV);

WriteMovie('ShapeData_points',MOV);
