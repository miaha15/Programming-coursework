'http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-i'
'http://www.programiz.com/python-programming/examples/add-matrix'
'http://thesis.ljungblad.nu/2012/05/02/illustrating_matrix_factorisation/'
'http://science.slc.edu/~jmarshall/courses/2002/spring/cs50/BigO/'

'''
PSEUODO CODE
 
 A <- INPUT MATRIX
 B <- INPUT MATRIX
 
 C <- [[0,0,0],[0,0,0],[0,0,0]]
 D <- [[0,0,0],[0,0,0],[0,0,0]]
 E <- [[0,0,0],[0,0,0],[0,0,0]]
 F <- [[0,0,0],[0,0,0],[0,0,0]]
 

 ADDIT [A,B]
 
repeat
 FOR r <- TO(len(A)) DO 
// A[0] selects the entire row starting from the top of the list
     FOR c <- TO(len(B[0])) DO 
         C[r][c] <- A[r][c] + B[r][c]
     end for
 end for
 RETURN C

  MULTI [A,B]
 
repeat
 FOR r <- TO(len(A)) DO 
     FOR c <- TO(len(B[0])) DO
       FOR k <- TO(len(B)) DO
         D[r][c] <- A[r][k] + B[k][c]
       end for
     end for
 END for
 RETURN D

  SCALE [C,C]
 
repeat
 FOR r <- TO(len(A)) DO 
     FOR c <- TO(len(A[0])) DO 
         E[r][c] <- C[r][c] + C[r][c]
     end for
 end for
 RETURN E
 
  SUBT [C,D]
 
repeat
 FOR r <- TO(len(C)) DO 
// A[0] selects the entire row starting from the top of the list
     FOR c <- TO(len(D[0])) DO 
         F[r][c] <- C[r][c] + D[r][c]
     end for
 end for
 FOR r <- F DO
   OUTPUT r
 RETURN F
 

 CALL ADDIT(A, B)
 CALL MULTI(A, B)
 CALL SCALE(C, C)
 CALL SUBT(C, D)
 
'''

'''
Result of each function is stored in a seperate variable
Each variable is called to its appropriate function when needed
*2 was achieved by adding the matrix to itself which is the same as *2
The end result matrix is outputted line by line for the user
Matrix and result matrix are all global so that they are available to all
functions

'''

import sys

MatrixOne = [[10,20,10],[9,10,9],[20,30,40]] #1
MatrixTwo = [[20,50,10],[60,70,10],[10,80,10]] #1

ResultMatrix1 = [[0,0,0],[0,0,0],[0,0,0]]#1
ResultMatrix2 = [[0,0,0],[0,0,0],[0,0,0]]#1
ResultMatrix3 = [[0,0,0],[0,0,0],[0,0,0]]#1
ResultMatrix4 = [[0,0,0],[0,0,0],[0,0,0]]#1


def Addit(B,C):
    for row in range(len(B)): #n
        for column in range(len(C[0])): #n^2
            ResultMatrix1[row][column] = B[row][column] + C[row][column] #1n^2
    return ResultMatrix1


def Multi(B,C):
    for row in range(len(B)): #n
        for column in range(len(C[0])): #n^2
            for Loop in range(len(C)): #n^3
                ResultMatrix2[row][column] += B[row][Loop] * C[Loop][column]#1n^3
    return ResultMatrix2
        
def Scale(B,C):
    for row in range(len(B)): #n
        for column in range(len(C[0])): #n^2
            ResultMatrix3[row][column] = B[row][column] + C[row][column] #1n^2
    return ResultMatrix3


def Subt(B,C):
    for row in range(len(B)): #n
        for column in range(len(C[0])): #n^2
            ResultMatrix4[row][column] = B[row][column] - C[row][column] #1n^2
    for result in ResultMatrix4: #n
        print(result) #1n
    return ResultMatrix4


Addit(MatrixOne, MatrixTwo)
Multi(MatrixOne, MatrixTwo)
Scale(ResultMatrix1, ResultMatrix1)
Subt(ResultMatrix2, ResultMatrix3)


sys.exit

'''

A = B*C - 2 * (B+C)

// B and C must be multiplied first
A1 <- MULTIPLY_MATRIX1 (B,C)

// B + C must be added next
A2 <- ADDITION_MATRIX1 (B,C)

// The addition of B and C (stored in A2) must be multiplied by 2

// A2 is multiplied by 2
A3 <- MULTIPLY_NA (A2,2)

// Values of A1 and A3 are added and stored in R
R <- A1 + A3

'''

#What is the run-time (BigO notation?)

'''
I can see that my program had a notation of 5n +6 + 7n^2 + 2n^3
We can ignore the +6, 5n and 7n^2 as they have a smaller magnitude in comparison to 2n^3
2n^3 has a larger magnitude and so is more important and significant
When it comes to program efficiency
On a graph 2n^3 is equivalent to the O(n^3)
'''
