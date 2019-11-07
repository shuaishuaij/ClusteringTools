#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
'''
@author: jwli9
@contact: jwli9@iflytek.com

根据中心点到点的欧氏距离进行聚类, 适用于Euclidean数据, 对非欧数据的效果不好
'''

from sklearn.cluster import KMeans

class kmeans(object):
        def __init__(self,features, n_clusters, random_state=True):
                self.features = features
                self.n_clusters = n_clusters
                self.random_state = random_state
                self.run()
        def run(self):
                self.kmeans_model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state).fit(self.features)
                self.output = self.kmeans_model.labels_

        def predict(self, new_feature):
                self.predict_output = self.kmeans_model.predict(new_feature)


