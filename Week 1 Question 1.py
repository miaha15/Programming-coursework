"https://www.tutorialspoint.com/python/python_lists.htm"
"https://www.tutorialspoint.com/python/python_functions.htm"
"http://stackoverflow.com/questions/3540431/difference-between-random-randint-vs-randrange"
"http://code.activestate.com/recipes/360461-fisher-yates-shuffle/"

'''
Variable stores the size of the list
Picks a random item from the list
Swaps the items in a list to create a new rearranged list
Returns the final value of x back to the function    
Calls the function along with the list contents
Prints the new randomly rearranged list
'''

import sys
import random

def Shuffle(x):
    size = len(x)#1
    for counter in range (size): #n
        RandomShuffle1 = random.randrange(0,size) #1n
        RandomNShuffle2 = random.randrange(0,size) #1n
        x[RandomShuffle1],x[RandomNShuffle2] = x[RandomNShuffle2],x[RandomShuffle1]#1n
    return x #1

List = [1,8,9,7,10,20,44] #1
Shuffle(List) #1
print(List) #1

sys.exit()

'''
I can see that my program had a notation of 4n +5
We can ignore the +5 as it has a smaller magnitude in comparison to 4n
4n has a larger magnitude and so is more important and significant
When it comes to program efficiency
On a graph 4n is equivalent to the (O)n linear graph
'''
