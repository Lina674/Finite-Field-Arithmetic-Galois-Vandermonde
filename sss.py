#input: secret S, num of shares n, threshold k
#output: n shares (xi,yi)

#random polynomial degree k-1 s.t. p(0)=S
import random
import numpy as np

# p = np.poly1d([1, 2, 3, 4]) deg 3
# print(p)
def generation(m,S,n,k):
    coeff = []
    for i in range(k-1):
        coeff.append(random.randint(1,2**m-1)) #GF(2**m)
    coeff.append(S)
    poly = np.poly1d(coeff)
    print(poly)
generation(3,1,2,3)