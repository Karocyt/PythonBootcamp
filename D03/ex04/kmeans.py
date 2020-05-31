import numpy as np 
from numba import jit
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from csvreader import CsvReader

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def l1loss(self, x, y_pred):
        # print(self.centroids[y_pred[1]].shape, x[1].shape)
        # print(self.centroids[y_pred[1]], x[1])
        # y = y_pred[1]
        # test = self.centroids[y_pred[1]] - x[1]
        dist = np.array([np.abs(self.centroids[y_pred[i]] - x[i]) for i in range(len(x))])
        sq_dist = np.power(dist, 2)
        return sq_dist.sum()

    #@jit(forceobj=True)    
    def fit(self, X, plot=False):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """

        # Normalization
        X = X.copy()
        self.min = [X[:,0].min(), X[:,1].min(), X[:,2].min()]
        X -= self.min
        self.max = [X[:,0].max(), X[:,1].max(), X[:,2].max()]
        X /= self.max

        # Random init centroids
        if len(self.centroids) == 0:
            self.centroids = np.array([X[np.random.randint(0, len(X))] for i in range(self.ncentroid)])
        #print("centroids", self.centroids)

        

        
        for iteration in range(self.max_iter):
            # Prediction
            y_pred = np.array([self.predict_one(x) for x in X])
            print("y_pred:", y_pred)

            # Plot (optionnal)
            if plot:
                ax = plt.axes(projection='3d')
                col = "rgbm"
                ax.scatter3D(X[:,0], X[:,1], X[:,2], color=[col[c] for c in y_pred])
                for i, c in enumerate(self.centroids):
                    ax.scatter3D(c[0], c[1], c[2], color=col[i], s=200)
                plt.show()

            # Centroids update
            print("y_pred", y_pred)
            for i in range(self.ncentroid):
                assigned = np.array([elem for j, elem in enumerate(X) if y_pred[j] == i])
                #print("assigned", assigned)
                if len(assigned) > 0:
                    self.centroids[i] = np.array(
                        [assigned[...,j].mean() for j in range(len(self.centroids[i]))])

            #print("centroids", self.centroids)
        print("end fit")
        return self.l1loss(X, y_pred)

    #@jit(forceobj=True)
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
          This function should not raise any Exception.
        """
        X = X.copy()
        X -= self.min
        X /= self.max
        
        return np.array([self.predict_one(x) for x in X])

    def predict_one(self, x):
        best = 0
        best_dist = np.abs(self.centroids[best] - x).sum()
        for i, c in enumerate(self.centroids[1:]):
            tmp = np.abs(c - x).sum() #
            if tmp < best_dist:
                best_dist = tmp
                best = i + 1
        #print(best)
        return best

if __name__ == "__main__":
    # constants
    data = None
    citizenships =[
        "The flying cities of Venus",
        "United Nations of Earth",
        "Mars Republic",
        "Asteroids' Belt colonies"
    ]
    
    # Init
    k = KmeansClustering(max_iter=10, ncentroid=len(citizenships))
    with CsvReader("../assets/solar_system_census.csv", header=True) as f:
        data = np.array(f.getdata())
    workbench = np.array([list(elem.values()) for elem in data.copy()])[:,1:].astype(np.float)

    # Fit
    k.fit(workbench, plot=True)

    # Prediction
    y_pred = k.predict(workbench)
    print(y_pred, y_pred.shape)

    # Reformatting
    res = list(data)
    for i, y in enumerate(y_pred):
        res[i]['citizenship'] = citizenships[y]
    print(np.array(res).shape)
    print(res)
