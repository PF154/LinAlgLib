class Matrix:
    def __init__(self, rows, columns):
        self.matrix = [[0 for i in range(columns)] for i in range(rows)]
        self.size = (rows, columns)
    
    def determinant(self):
        # For now, we just do a 2x2 determinant. This will be updated later
        return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
    
    def __add__(self, other):
        # first check to make sure that matricies are the same size
        if (self.size != other.size):
            raise ValueError("Tried to add two matrices of different sizes")
        
        # add by element
        sum_matrix = Matrix(self.size[0], self.size[1])
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                sum_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return sum_matrix

    def __sub__(self, other):
        if (self.size != other.size):
            raise ValueError("Tried to add two matices of different sizes")
        
        # subtract each element respectively
        difference_matrix = Matrix(self.size[0], self.size[1])
        for i in range(self.size[0]):
            for j in range(self.size[0]):
                difference_matrix.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        
        return difference_matrix

    def __mul__(self, other):
        # make sure that sizes of matrices are compatible
        if (self.size[1] != other.size[0]):
            raise ValueError("Tried to multiply matrices of incompatible sizes")
        
        product_matrix = Matrix(self.size[0], other.size[1])
        for i in range(self.size[0]):
            # i is the index of the row in matrix self
            # we want to dot prod the row with each column of matrix other.
            # each dot prod should become a successive element in the first row of product_matrix
            for j in range(other.size[1]):
                # j is the index of a column in other
                dp = 0
                for k in range(other.size[0]):
                    # k is the index of an element in column j
                    dp += self.matrix[i][k] * other.matrix[k][j]
                product_matrix.matrix[i][j]

        return product_matrix


    def __str__(self):
        return_string = "["
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                return_string += " " + str(self.matrix[i][j]) + ","
            return_string += "\n "
        return return_string[:-2] + " ]"


# Functions to add
'''subtract
multiply
divide?
eigenpairs
inverse
transpose
transformation
echelon form
'''

# Create two 3x3 matrices
m1 = Matrix(3, 3)
for i in range(3):
    for j in range(3):
        m1.matrix[i][j] = i + j

print(m1)

m2 = Matrix(3, 3)
for i in range(3):
    for j in range(3):
        m2.matrix[i][j] = i * j

print(m2)

print(m1 * m2)