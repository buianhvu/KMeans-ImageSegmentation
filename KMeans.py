import numpy as np
import random
import math
class KMeans:
    def cluster(self, K, ImgArr, cuttoff):
        centroids = []
        new_centroids = []
        list_of_elements_in_each_cluster = [[] for l in range (K)]
        result = []
        num_of_pixels = ImgArr.shape[0]
        #choose randomly initialial centroids
        for i in range (K):
            pos = random.randint(0, num_of_pixels)
            centroids.append(ImgArr[pos])

        #loop_count is the time we have to try to find the final centroids
        loop_count = 0
        # loops until meet the stop condition that the biggest shift is not over cutoff
        while True:
            loop_count += 1
            #traverse all elements in dataset
            for eIndex in range (ImgArr.shape[0]):
                smallest_distance = self.getDistance(ImgArr[eIndex], centroids[0])
                clusterIndex = 0
                #find the closest centroid for a pixel
                for k in range (K-1):
                    distance = self.getDistance(ImgArr[eIndex], centroids[k+1])
                    if(distance < smallest_distance):
                        smallest_distance = distance
                        clusterIndex = k + 1
                list_of_elements_in_each_cluster[clusterIndex].append(ImgArr[eIndex])
                result.append(clusterIndex)
            #find new centroids
            for cIndex in range(len(list_of_elements_in_each_cluster)):
                array_of_pixels = list_of_elements_in_each_cluster[cIndex]
                array_of_pixels = np.array(array_of_pixels)
                new_centroid = np.sum(array_of_pixels, axis = 0)/(array_of_pixels.shape[0])
                # print ' new_ centroid'
                # print new_centroid
                new_centroids.append(new_centroid)
            print new_centroids
            # raw_input()

            print 'count = %d' % (loop_count)
            print 'old centroids'
            print centroids
            print 'new centroids + len %d' %(len(new_centroids))
            print new_centroids

            #biggest_shift is the biggest distance between two set of old and new centroids
            biggest_shift = 0
            for index_cluster in range(K):
                # print '^'
                # print new_centroids[index_cluster]
                shift = self.getDistance(new_centroids[index_cluster], centroids[index_cluster])
                print'shift %f' %(shift)
                biggest_shift = max(biggest_shift, shift)
            print 'biggest shilft %f' %(biggest_shift)
            if biggest_shift < cuttoff :
                print 'done analysing'
                # for re in range (len(result)):
                #     print 'result : '
                #     print result[re]
                # print ' result'
                return result, new_centroids
                break;
            else :
                centroids = new_centroids
                new_centroids = []
                result = []

    def getDistance(self, X, Y):
        # print 'x'
        # print X
        distance = 0
        # print type(X)
        # print type(Y)
        # print X.shape
        # print Y.shape
        for i in range(len(X)):
            # print type(X[i])
            _sum = (int(X[i]) - int(Y[i]))#math.pow((X[i] - Y[i]), 2)
            _sum *= _sum
            distance += _sum
        # distance = np.sum(np.abs(X - Y), axis=1)
        return math.sqrt(distance)
    # def getDistance(self, X, Y):
    #     distance = np.linalg.norm(X - Y)
    #     # distance = np.sum(np.abs(X - Y), axis=1)
    #     return distance

