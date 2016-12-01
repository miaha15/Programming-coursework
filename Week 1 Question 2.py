'http://stackoverflow.com/questions/766141/reverse-a-string-in-python'
'http://stackoverflow.com/questions/4502429/recursive-factorial-function'
'http://stackoverflow.com/questions/73663/terminating-a-python-script'
'Dianas Lecture Slides'

import sys
Factorial = int(input("Factorial of: "))

'''
The user inputs is imported when the function 'factorialCalc' is called
The user inputs an integer
If the user enters 1 then the program will output 1
If the user enters zero the program wont crash and it will output 0 instead
After the calculation the value is returned back to the variable of the function
Which is then stored in the variable called 'Carry'
The end value will then be printed for the user
The next function is called 'TrailingZeros' with the value of 'Carry' being
Imported from the previous function where the factorial result was stored
Value of the variable 'Carry' is covertedto string so it can operate with
The string manipulation correctly
'Increments' is initialised to 0
for each character in the string being read backwards if a '0' is found it will
Increase the 'Increment' value stored by +1 resulting in the '0's being recorded
Once the character is not a '0' then it will go to the ELSE statement.
If a negative number inputted then it will output a message saying so.
'Break' insures that the line previous, once executed, instantly returns
Back to the function
'''
def factorialCalc (x):
    
    if x==1:
        return 1 #1
    elif x==0:
        return 0 #1
    elif x<0:
        return print("Must be a positive number") #2
    else:
        return x * factorialCalc(x-1) #1

Carry = factorialCalc(Factorial) #1
print ('Factorial of' ,Factorial, 'is:' ,Carry) #1


def TrailingZeros(y):
    string = str(Carry)#1
    increments = 0 #1
    for i in string [::-1]: #n
        if i == "0": #1n
            increments = increments + 1 #1n
        else:
            print('Number of trailing zeros:' ,increments)#1
            break

factorialCalc(Factorial)#1
TrailingZeros(Carry)#1

sys.exit()

'''
I can see that my program had a notation of 3n +12
We can ignore the +12 as it has a smaller magnitude in comparison to 3n
3n has a larger magnitude and so is more important and significant
When it comes to program efficiency
On a graph 3n is equivalent to the (O)n linear graph
'''
