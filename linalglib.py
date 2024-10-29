class Matrix:
    def __init__(self, columns, rows):
        self.matrix = [[0 for i in range(columns)] for i in range(rows)]
        # change this to
        # for i in range(rows):
        #     for j in range(columns):
        #         new_row = []
        #         new_row.append = 0
        self.size = (columns, rows)
    
    def determinant(self):
        # For now, we just do a 2x2 determinant. This will be updated later
        return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
    
    def __add__(self, other):
        # first check to make sure that matricies are the same size
        if (self.size != other.size):
            # change this to raise TypeError eventually
            print("ERROR! Tried to add two matrices of different sizes")
            return Matrix(3, 3)
        
        # add by element
        sum_matrix = Matrix(3, 3)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                sum_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return sum_matrix

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

print(m1 + m2)