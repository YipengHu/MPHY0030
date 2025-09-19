# class file for iterative closest point algorithm

import numpy as np
from scipy.spatial import cKDTree as kdtree


class IterativeClosestPoint:

    def __init__(self, px, py):
        self.pointset_x = px
        self.pointset_y = py
        self.transform = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,0]])
        self.maxIter = int(1e3)
        self.tolD = 1e-5
        self.kdtree = kdtree(px)


    def register(self):
        self.transform[3,:] = np.mean(self.pointset_x,axis=0) - np.mean(self.pointset_y,axis=0)
        tmp_dist = np.inf
        for ii in range(self.maxIter+1):
            # apply current transform
            tmp_pointset_y = self.apply_transform(self.pointset_y, self.transform)
            # find the closest points
            _, idx = self.kdtree.query(tmp_pointset_y, k=1)
            # compute the transformation
            self.transform, dist = self.compute_transform(self.pointset_x[idx,:],self.pointset_y)
            print('Iter=%d, d=%f.' % (ii, dist))
            if np.abs(dist-tmp_dist) < self.tolD:
                print('Tolerance in residual distance change (%f) reached.' % self.tolD)
                break
            else:
                tmp_dist = dist


    @staticmethod
    def apply_transform(y,tform):
        return np.matmul(y,tform[:-1,]) + tform[3,np.newaxis]


    @staticmethod
    def compute_transform(x,y,correct_reflect=True):
        x_mean = np.mean(x,axis=0,keepdims=True)
        y_mean = np.mean(y,axis=0,keepdims=True)
        nx = x-x_mean
        ny = y-y_mean
        # absolute rotation
        v,_,u = np.linalg.svd(np.matmul(nx.transpose(),ny))
        if correct_reflect:
            rot = np.matmul(
                np.matmul(v,
                [[1,0,0],
                [0,1,0],
                [0,0,np.linalg.det(np.matmul(v,u.transpose()))]]),
                u.transpose())
        else:
            rot = np.matmul(v,u.transpose())
        # translation
        tform = np.concatenate([rot,x_mean-np.matmul(y_mean,rot)],axis=0)
        d = np.sqrt(np.mean(np.sum(np.square(np.matmul(y,rot)+tform[3,np.newaxis]-x),axis=1)))
        return tform, d
