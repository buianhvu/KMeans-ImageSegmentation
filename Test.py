import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from KMeans import KMeans

def main():
    #opening image
    img = mpimg.imread('girl6.jpg')
    # now an image is stretched out into a array, each pixel is an array of three numbers.
    x = img.reshape(img.shape[0] * img.shape[1], 3)
    kmeans = KMeans()
    result, centroids = kmeans.cluster(3, x, 0.2)
    for i in range(len(x)):
        cluster_index = result[i]
        x[i] = centroids[cluster_index]
    x = x.reshape(img.shape[0], img.shape[1], img.shape[2])
    plt.imshow(x)
    plt.axis('off')
    plt.show()

main()
# print img
