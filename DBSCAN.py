#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
'''
@author: jwli9
@contact: jwli9@iflytek.com

根据密度进行聚类, 适用于所有类型数据
'''
from sklearn.cluster import DBSCAN

class dbscan(object):
        def __init__(self,features, eps, min_samples):
                self.features = features
                self.eps = eps
                self.min_samples = min_samples
                self.run()
        def run(self):
                self.output = DBSCAN(eps=self.eps,
                                         min_samples=self.min_samples,
                                         metric='seuclidean',
                                         algorithm='auto').fit_predict(self.features)
                assert len(self.output) == len(self.features)













































