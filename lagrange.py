import numpy as np
from vandermonde import GF
# p = np.poly1d([1, 2, 3, 4])
# print(p)

# roots = [1, 2]
# poly = np.poly1d(roots, True)
# print(poly)
class Lagrange:
    def __init__(self, gf) :
        self.gf = gf
    
    def lagrange_polynomial(self, x_values, y_values):
        """
        x_values is the array containing the x values of your set of coordinates
        y_values is the array containing the y values of your set of coordinate
        {(1,2), (3,4)} --> x_values, y_values = [1,3], [2,4]
        """
        
        # x_values = [0,1,2]
        # y_values = [2,1,4]

        n = len(x_values)
        polynomial = np.poly1d([0])

        for i in range(n):
            roots = []
            roots.extend(element for element in x_values if element != x_values[i])
            factor = 1
            for j in range(n):
                if i != j:
                    factor *= x_values[i]-x_values[j]
            p_roots = (y_values[i]*np.poly1d(roots, True))/factor
            polynomial += p_roots
        return polynomial
            

# print(Lagrange([0,1,2],[2,1,4]))
# print(Lagrange([-2,1,3,7],[5,7,11,34]))

gf = GF(3, 0b1011)  # Initialize GF(2^3) with primitive polynomial 0b1011
lagrange = Lagrange(gf)

x_values = [0, 1, 2]
y_values = [2, 1, 4]

polynomial = lagrange.lagrange_polynomial(x_values, y_values)
