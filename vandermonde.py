class GF:
    def __init__(self, m, poly) :
        self.m = m
        self.poly = poly
        self.field_size = 1 << m

    def add(self,n1,n2):
        return (n1^n2)

    def multiply(self,n1,n2): 
        prod = 0
        while n2 > 0:
            if n2 & 1:
                prod ^= n1
            n2 >>= 1
            n1 <<= 1
            if n1 & (1 << self.m):
                n1 ^= self.poly
        return prod % self.field_size
    
    def exponent(self,n1,exp):
        prod = 1
        for i in range(exp):
            prod = self.multiply(prod,n1)
        return prod % self.field_size #(prod % (1 << m))
    
 
# print(multiply(3,3,3,0b1011))
# print(add(3,5))
# print(multiply(2,2,3,0b1011))

# print(exponent(5,2,3,0b1011))
# print(exponent(3,2,3,0b1011))
# print(exponent(3,3,3,0b1011))
# print(exponent(2,2,3,0b1011))

class Vandermonde:
    def __init__(self, gf) :
        self.gf = gf

    def Vandermonde(self,n,k): #ex: GF(2^m), n is message length and k is redundancy length
        """
        Returns Vandermonde matrix with n columns and n+k rows (n is the message length and k is the number of redundancy bits).
        """
        #n+k rows, n columns
        #[[0 1]
        #[2 3]]    2x2 matrix
        #2^1 2^2 2^3 ... 2^(n-1)
        #i i*i i*i*i ... i**(n-1)
        matrix = []

        for i in range(n+k):
            row = []
            for j in range(n):
                if j==0:
                    row.append(1)
                else:
                    row.append(self.gf.exponent(i,j))
            matrix.append(row)
        return matrix
    #top nxn matrix must be an identity matrix
    
    def dot_product(self, u,v): #u and v are vectors
        sum = 0
        if len(u)==len(v):
            for i in range(len(u)):
                prod = self.gf.multiply(u[i], v[i])
                sum = self.gf.add(sum, prod)
            return sum
        else:
            raise Exception(f"The two vectors must have equal length")
    
    def colonize_matrix(self,matrix):
        colonized_matrix = []
        for i in range(len(matrix[0])): #nber of rows     #for i in range len(matrix2), for j in range len(matrix2[0])
            col = []
            for j in range(len(matrix)): #nber of cols
                col.append(matrix[j][i])
            colonized_matrix.append(col)
        return colonized_matrix

    def matrix_product(self,matrix1, matrix2):
        result_matrix = []
        for row in matrix1:
            result_row = []
            for column in self.colonize_matrix(matrix2):
                entry = self.dot_product(row, column)
                result_row.append(entry)
            result_matrix.append(result_row)
        return result_matrix
    
#v = Vandermonde(3,3,5,0b1011)

matrix1 = [[1,1], [2,2]]
matrix2 = [[3,5], [6,7]]
matrix3 = [[1,2,3], [4,5,6], [10,12,11]]
#print(v)
p = Vandermonde(GF(3,0b1011)).colonize_matrix([[1,2,3]])
#print(len(p[0]))

#print(Vandermonde(GF(3,0b1011)).Vandermonde(3,5))
#print(dot_product(matrix1[0], matrix2[0], 3, 0b1011))


    #return colonized_matrix2

#print(matrix_product(matrix1, matrix2, 3, 0b1011))

# def get_minor(matrix, i, j):
#     """
#     i := row
#     j := column
#     """
#     matrix.pop(i)
#     m = colonize_matrix(matrix)
#     m.pop(j)
#     return colonize_matrix(m)

# #print(get_minor(matrix3, 0, 2))

# def determinant(matrix, m, poly):
#     m, n = len(matrix), len(matrix[0])
#     if m != n:
#         raise Exception("The matrix must be a square matrix")
#     else:
#         if n == 2:
#             return add(multiply(matrix[0][0], matrix[1][1], m, poly), multiply(matrix[0][1], matrix[1][0], m, poly)) #WRONG

# matrix4 = [[1,2], [3,4]]

# print(determinant(matrix4, 3, 0b1011))