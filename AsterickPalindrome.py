#This one isn't leetCode it was Just an interview question that I couldn't get at the time cause I was nervous :(
#Difficulty: Easy
#Description: Basically it is the same as checking a valid palindrome. The exception is that the str contains an * for one of the 
#characters instead of the character itself ex: raceca* where the final r is replaced.

#If there are more than 2 letters replaced than the str equates to false. I don't know some of the edges cases or how specific it should be
#but from the view test cases I saw, assume Str is at least 6 letters of longer.

#Progress: Completed/Check for Edge cases


def asterick(word : str):
    Asterickcount = 0
    for i in range(len(word)):
        if Asterickcount>1:
            return(False)
            
        if word[i] != word[len(word)-1-i]:
            if word[i] == '*' or word[len(word)-1-i] == '*':
                Asterickcount +=1
                continue
            return(False)

    return(True)
print(asterick('Raceca*'))
