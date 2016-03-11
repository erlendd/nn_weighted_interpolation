# About
A simple python class to perform a weighted nearest-neighbour based interpolation of data.
This method is an extremely simple (yet robust) method to take coarse, randomly distributed
data in the form (X, y) and give smooth predictions of the y-values for values of X that are 
not explicitly known. 

The X data above can be of arbitrary dimensionality, e.g. if we wanted to interpolate the 
temperature along the length of a 5 metre long room, meaured every 1 metre then X = {1, 2, 3, 4, 5} 
and y could just contain the corresponding temperature measurements. We could equally-well generalise 
to measurements along the width of the room and at different heights, i.e. 
X = { [l1, w1, h1,], [l2, w2, h2], ... [l5, w5, h5] }, where l, w, h indicate length, width and height
measurements respectively.

My own reason to write this was to re-align large datasets of molecular energies (computed 
using [density functional theory](https://en.wikipedia.org/wiki/Density_functional_theory)) to a 
perfect grid, vastly simplifying the use of other interpolation methods.
** Requirements: python 2.7 **

# Example usage
The code is quite simple and with useful comments, so the best way to undestand what it 
does is with a toy example.
```python
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
```

