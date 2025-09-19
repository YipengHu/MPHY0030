# script_icp

import numpy as np
from icp import IterativeClosestPoint as ICP
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


px = np.genfromtxt('../data/points_x.csv',delimiter=',')
py = np.genfromtxt('../data/points_y.csv',delimiter=',')

objICP = ICP(px,py)
objICP.register()
py_transformed = objICP.apply_transform(py,objICP.transform)


# plot
trix = np.genfromtxt('../data/tris_x.csv',delimiter=',')-1
triy = np.genfromtxt('../data/tris_y.csv',delimiter=',')-1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(px[:,0], px[:,1], px[:,2], triangles=trix, color='b')
ax.plot_trisurf(py[:,0], py[:,1], py[:,2], triangles=triy, color='r')
ax.plot_trisurf(py_transformed[:,0], py_transformed[:,1], py_transformed[:,2], triangles=triy, color='g')
plt.show()
# plt.savefig('icp.png')
