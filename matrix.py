import random
from copy import deepcopy

class MatrixError(Exception):
    pass

class Matrix:

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.outer = []
        
        for i in range(nrows):
            self.inner = []
            for j in range(ncols):
                self.inner.append(random.randint(0,9))
            self.outer.append(self.inner)

    def add(self, m):
        """return a new Matrix object after summation"""
        matrix_add = Matrix(self.nrows, self.ncols)
        
        for i in range(len(self.outer)):
            for j in range(len(self.outer[i])):
                matrix_add.outer[i][j] = 0
                matrix_add.outer[i][j] = self.outer[i][j] + m.outer[i][j]

        return matrix_add

    def sub(self, m):
        """return a new Matrix object after summation"""
        matrix_sub = Matrix(self.nrows, self.ncols)
        
        for i in range(len(self.outer)):
            for j in range(len(self.outer[i])):
                matrix_sub.outer[i][j] = 0
                matrix_sub.outer[i][j] = self.outer[i][j] - m.outer[i][j]

        return matrix_sub

    def transpose(self):
        """return a new Matrix object after transpose"""
        matrix_transpose = Matrix(self.ncols,self.nrows)

        for i in range(len(self.outer)):
            for j in range(len(self.outer)):
                matrix_transpose.outer[i][j] = 0
                matrix_transpose.outer[i][j] = self.outer[j][i]
  
        return matrix_transpose
   

    def mul(self,m):
        """return a new Matrix object after multiplication"""
        matrix_mul = Matrix(self.nrows, m.ncols)
    
        for i in range(self.nrows):
            for j in range(m.ncols):
                matrix_mul.outer[i][j] = 0
                for k in range(self.ncols):
                    matrix_mul.outer[i][j] += A.outer[i][k]*m.outer[k][j]
       
        return matrix_mul
        
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.nrows):
            for j in range(self.ncols):
                print (self.outer[i][j], end=' ')
            print('')
        
        
Arows = input('Enter A matrix\'s rows:')
Acols = input('Enter A matrix\'s cols:')

A = Matrix(int(Arows),int(Acols))
print('Matrix A ' + '('+ str(Arows) +', '+ str(Acols) + '):' + '\n' )
A.display()

Brows = input('Enter B matrix\'s rows:')
Bcols = input('Enter B matrix\'s cols:')

B = Matrix(int(Brows),int(Bcols))

print('Matrix B ' + '('+ str(Brows) +', '+ str(Bcols) + '):' + '\n' )
B.display()

print('='*10 + ' A + B ' + '='*10 )
C = A.add(B)
C.display()

print('='*10 + ' A - B ' + '='*10 )
D = A.sub(B)
D.display()

print('='*10 + ' A * B ' + '='*10 )
E = A.mul(B)
E.display()

print('='*5 + ' the transpose of A * B ' + '='*5 )
F = A.mul(B)
F.transpose().display()




