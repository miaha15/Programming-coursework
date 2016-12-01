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
