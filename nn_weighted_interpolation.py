
from numpy import linalg as LA
import numpy as np

class NNWeightedInterpolation:

    def __init__(self, X, y, p=6):
        self.X = X
	self.y = y
	self.p = p
	self.dims = len(X[0])

    # computes the Euclidean distance between two points a and b in space
    def euclid_dist(self, a, b):
        assert len(a) == len(b)
        return LA.norm(np.array(a)-np.array(b))

    def findFeatureIdx(self, testpointls):
        try:
	    idx = self.X.index( testpointls )
	except ValueError:
	    idx = None
	return idx

    def interpolate(self, testpointls):
        assert len(testpointls) == self.dims
	# First, check if the point was in the training set, use it directly if so
        idx = self.findFeatureIdx( testpointls )	
	if not idx == None:
	    return self.y[idx]
	# Not in training set, need all distances...
	partfn = 0.0
	vote = 0.0
        for i in range(len(self.X)):
	    dist = self.euclid_dist( testpointls, self.X[i] )
	    weight = 1.0/dist**self.p
	    partfn = partfn + weight
	    vote = vote + self.y[i]*weight
	
	return vote/partfn




# Example usage...
if __name__ == "main":

    # very coarse raw (input) data...
    myX = [[0,0],[0,1],[1,0],[1,1]]
    myy = [0, 1, 1, 4]
   
    # create our interpolation object, loading in our
    # independent (myX) and dependent (myY) data...
    nn = NNWeightedInterpolation( myX, myy, 2)
    
    # now interpolate this data to a much finer grid
    # her we use 0.05 increments...
    for x in range(0,21):
        for y in range(0,21):
            thisy = nn.interpolate( [ (x/20.0)*1, (y/20.0)*1 ] )
            print x*1/20.0, y*1/20.0, thisy

