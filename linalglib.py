class Matrix:
    def __init__(self, rows, columns):
        self.matrix = [[0 for i in range(columns)] for i in range(rows)]
        self.size = (rows, columns)
    
    def determinant(self):
        if (self.size[0] != self.size[1]):
            raise ValueError("Tried to compute the determinant of a non-square matrix")
        
        # base case
        if (self.size[0] == 2):
            print(" Determinant of ")
            print(self)
            print(" is " + str(self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]))
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        
        # Later, we can change this to compute based on the row with the most zeros.
        # For now, I think brute force is just fine
        det = 0
        for i in range(self.size[1]): # Each i is a column in the first row
            sub_matrix = Matrix(self.size[0] - 1, self.size[1] -1) # create empty matrix to store values in

            for row in range(1, self.size[0]): # Expand on first row by convention, therefore skip in further calculations
                idx = 0 # Keep track of the position in the sub_matrix to add to
                for column in range(self.size[1]): # Iterate over each column of the main matrix
                    if (column != i): # If the column should be included
                        sub_matrix.matrix[row - 1][idx] = self.matrix[row][column] # Add that column to the sub-matrix
                        idx += 1 # Increment our sum_matrix index

            # print("Adding to determinant: " + str(self.matrix[0][i] * sub_matrix.determinant() * ((-1) ** (i+2))))
            det += self.matrix[0][i] * sub_matrix.determinant() * ((-1) ** (i+2))

        return det
    
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
        if isinstance(other, Matrix):
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
                    product_matrix.matrix[i][j] = dp

            return product_matrix
        
        elif isinstance(other, int) or isinstance(other, float):
            product_matrix = Matrix(self.size[0], self.size[1])

            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    product_matrix.matrix[i][j] = other * self.matrix[i][j]

            return product_matrix
        
        else:
            raise TypeError("Tried to multiply matrix by an unsupported type")
    
    def transpose(self):
        transpose_matrix = Matrix(self.size[1], self.size[0])

        for i in range(self.size[0]): # Each i is the index of a row
            for j in range(self.size[1]): # Each j is the index of a column
                transpose_matrix.matrix[j][i] = self.matrix[i][j]
                
        return transpose_matrix
    
    def get_element(self, location):
        ''' Fetches element from matrix

                Parameters:
                    location (tuple):   The index (row, column) of the desired element

                Returns:
                    The element of the Matrix object's matrix at the specified index
        '''
        return self.matrix[location[0] - 1][location[1] - 1]

    def set_element(self, location, value):
        ''' Sets the value of a desired element in the matrix

                Parameters:
                    location (tuple):   The index (row, column) of the desired element
                    value (float):      The value to set at the specified index

                Returns:
                    No return value
        '''
        self.matrix[location[0] - 1][location[1] - 1] = value 

    def set_matrix(self, tdarray):
        ''' Sets the matrix of the Matrix object to a user defined 2D array
        

        '''
        # TODO: Figure out how to import this two-d array so that it doesn't reference the old one
        self.matrix = list(tdarray)

    def __str__(self):
        return_string = "["
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                return_string += " " + str(self.matrix[i][j]) + ","
            return_string += "\n "
        return return_string[:-2] + " ]"


# Functions to add
'''
import from 2d array
eigenpairs
inverse
transformation
echelon form
'''

# Create two 3x3 matrices
# m1 = Matrix(3, 3)
# for i in range(3):
#     for j in range(3):
#         m1.matrix[i][j] = i + j + 1

# print(m1)

# print(m1.determinant())

# m2 = Matrix(3, 3)
# for i in range(3):
#     for j in range(3):
#         m2.matrix[i][j] = i * j

# print(m2)

# m3 = m1 * m2

# print(m3)

# print(m3 * 7)

my_matrix = [[1, 2, 2], [14, 5, 3], [3, 4, 1]]
m2 = Matrix(3, 3)
m2.set_matrix(my_matrix)
print(m2)
my_matrix[1][1] = 9
print(my_matrix)
print(m2)