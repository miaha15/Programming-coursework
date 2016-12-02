'''
Premade list is given to the function
A for loop is used to step through the list
As it steps through each value of the list, it appends the list called TempList
If the current element is GREATER than the next element of the list
then it will check if everything stored in the TempList upto current element
is longer than the sequence stored in LongestSequence
If it is then it will be overwritten, else it will ignore.
'''

import sys

def SubSequence(List):
    TempList = []
    LongestSequence = ("")
    
    for element in range(0, len(List)-1):
        
        TempList.append(List[element])
    
        if List[element] > List[element+1]:
            if len(TempList) > len(LongestSequence):
                LongestSequence = []
                LongestSequence = TempList
                TempList = []
                                           
    return LongestSequence

print('The Longest Sub-Sequence is:', SubSequence([1,2,3,4,1,2,3,4,5,0]))

sys.exit()
