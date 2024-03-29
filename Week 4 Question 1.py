'http://stackoverflow.com/questions/15193927/what-does-these-operators-mean-python'
'https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html'

'''
PSEUDO CODE

A <- user input
B <- user input
C <- user input

M <- in List[A,B,C]
  OUTPUT M

L <- user input
H <- user input

 BINARYSEARCH [x,y,z]
     StartPosition <- 0
     LastPosition <- length of [x] -1
     found = FALSE

     WHILE StartPosition EQUAL TO OR LESS THAN LastPosition DO
         IF LastPosition - StartPosition EQUAL TO OR LESS THAN 1 THEN
              RETURN FALSE

         MidPoint <- StartPosition + LastPosition // 2

         IF x[MidPoint] LESS THAN [y] AND x[MidPoint] GREATER THAN [z] THEN
             RETURN TRUE
             
         ELSE IF [y] LESS THAN OR EQUAL TO x[MidPoint] THEN
            LastPosition == LastPosition -1
             
         ELSE IF [z] GREATER THAN OR EQUAL TO x[MidPoint] THEN
                 StartPosition == StartPosition +1
                 
     RETURN FOUND
                 
                
 OUTPUT BINARYSEARCH[M,H,L]

'''

'''
User creates a list by entering start and end of list and what it goes up in
User then enters a Low and High interval Values to be searched within
Boolean is set to false at the start
Midpoint of the list is first found as a starting point
If midpointer is smaller than high interval and bigger than low interval
then we know there are values within the range and returns true
else if midpointer is equal to or higher than the high interval then
end of the list is reduced by 1 position to change the position of the midpointer
by 1 position to the left
If the midpointer is smaller than or equal to than the low interval then
start position is increased by one to move the pointer to the right by 1 place
once the condition of the while loop is reached then it will return the final
boolean value
'''


import sys

Start = int(input("Enter the starting number of your list: ")) #1
End = int(input("Enter the last number of your list: ")) #1
Sequence = int(input("Enter the sequence to go up in: ")) #1

ListMaker = list(range(Start,End,Sequence)) #1
print("Your Created List: ",ListMaker) #1

Low = int(input("Enter Lower Interval: ")) #1
High = (int(input("Enter Higher Interval: "))+1) #1

def BinarySearch(List,High, Low):
    StartPos = 0 #1
    LastPos = len(List) #1
    found = False

    while StartPos<=LastPos: #n
        if LastPos - StartPos <=1: #1n
            return False
    
        MidPointer = (StartPos + LastPos) // 2 #1n
        
        if List[MidPointer] < (High) and List[MidPointer] > (Low): #1n
            return True
        
        elif (High) <= List[MidPointer]: #1n
            LastPos = LastPos - 1 #1n

        elif (Low) >= List[MidPointer]:#1n
            StartPos = StartPos + 1 #1n
            
    return found

print(BinarySearch(ListMaker,High,Low)) #1

sys.exit

#What is the run-time (BigO notation?)
'''
I can see that my program had a notation of 7n +10
We can ignore the +10 as it has a smaller magnitude in comparison to 7n
7n has a larger magnitude and so is more important and significant
When it comes to program efficiency
On a graph 7n is equivalent to the O(n) Linear graph
worst case is O(logn)
'''
