'http://stackoverflow.com/questions/743806/split-string-into-a-list-in-python'
'http://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python'

'''
PSEUDO CODE

A <- User Input
B <- Function to split string at spacing stored as a List
C <- Empty List

 RECURSIVEF[x,y]
    IF [x] is empty THEN
        OUTPUT ("No Text Entered")
        RETURN [y]
    ELSE
        [y]appended to read next element in the List from the end
        Last element in [x]List is removed
        return back to the function [x,y]
        
 CALL RECURSIVEF
OUTPUT [C]

'''

'''
.split divides a string at the spacing and stored in Listing
List is read backwards and displayed for each element read and returned back
to the function
This is done by starting to read from the end of the list to the front
When returned back it is then  outputted for the user to see
'''

import sys

String = input("Enter text here ")
Listing = String.split()
Reversed = []

def RecursiveF(UserList, EmptyList):
    if UserList == []: #1
        return EmptyList #1
        print ("No Text Entered") #1
    else:
        EmptyList.append(UserList[-1]) #1
        UserList.pop(-1) #1
        return RecursiveF(UserList, EmptyList) #1

print(RecursiveF(Listing, Reversed)) #1


sys.exit()


'''
I can see that my program had a notation of +8
+8 is the only and largest magnitude and so is the only significant notation
When it comes to program efficiency
On a graph 8n is equivalent to the (O)n linear graph
'''
