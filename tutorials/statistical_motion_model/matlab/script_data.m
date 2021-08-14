%  &PlotMVData



%% load data
load('data_shapes');
MVData = cell2mat( ...
    cellfun(@(x) reshape(x,[],1),nodes_training,'UniformOutput',false) );

L = 200;
MVData_PCA = PCA_rec(MVData,MVData,L);



%% plot all data
figure,plot(MVData,'.')
figure,plot(MVData(:,1),'.')

%% plot mean and std of the first 100d
figure, 
errorbar( mean(MVData(1:100,:),2), std(MVData(1:100,:),[],2), '.');
grid on;

%% after PCA
figure, 
errorbar( mean(MVData_PCA(1:100,:),2), ...
    std(MVData_PCA(1:100,:),[],2), '.');
grid on;


