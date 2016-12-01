'http://stackoverflow.com/questions/25166338/recursive-function-to-remove-vowels'
'http://stackoverflow.com/questions/14330016/printing-a-function-in-python'

'''
PSEUDO CODE

 sentence <- user input

 VOWELREMOVER [x]
   IF length of [x] is EQUAL TO 0 THEN
      RETURN [x]
   ELSE IF "aeiouAEIOU" found in first letter of [x] THEN
       return letter at start of [x]
    return [x] AND APPEND string with start of letter in [x]   

 CALL VOWELREMOVER(sentence)
 OUTPUT (sentence)

'''

import sys
sentence = input("Input your sentence here ")

'''
Program first checks to see if theres an empty string
Checks to see if the first character is vowel
Skip first character and process rest
Return first character and process rest
'''

def VowelRemover (sentence):
    if len(sentence) == 0:
        return sentence
    elif sentence[0] in ("aeiouAEIOU"):
        return VowelRemover(sentence[1:])
    return sentence[0] + VowelRemover(sentence[1:])

print(VowelRemover(sentence))

sys.exit()
