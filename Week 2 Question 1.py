"http://www.programiz.com/python-programming/examples/square-root"
"http://stackoverflow.com/questions/17651384/python-remove-division-decimal"

'''
PSEUDO CODE

 user <- user input
 number <- user

 SQUARE [x]
   sqrt <- number ** 0.5
   insqrt <- (sqrt)
   answer <- (sqrt) * (sqrt)
//%d gets rid of the decimals while %0.3f counts to 3 decimal places
   output (number ,sqrt)
   output (answer)

 CALL SQUARE(number)

'''

import sys

user = input("input number ")
number = int(user)

'''
input is square rooted using ** power
function 'Square' is called with the variable value from 'number'
converts the float to a integer, gets rid of numbers after decimal
sqrt * sqrt is just multiplying itself by itself
%d gets rid of the decimals while %0.3f counts to 3 decimal places
'''

def Square(inputted):
    sqrt = number ** 0.5
    intsqrt = int(sqrt)
    answer = int(sqrt) * int(sqrt)
    print('The SQRT of %d is:  %0.3f'%(number ,sqrt))
    print('The Previous Perfect SQRT number is:',answer)
    
Square(number)

sys.exit()
