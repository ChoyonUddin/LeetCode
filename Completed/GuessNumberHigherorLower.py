#374. Guess Number Higher or Lower
#Difficulty: Easy
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

#Status: Completed

#Notes: Simple bin search, Guess is the api given ignore the function
'''
def guessNumber(self, n: int) -> int:
        high,low = n,1
        while low < high:
            mid = (high+low)//2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                high = mid 
            if guess(mid) == 1:
                low = mid + 1
        return low
def guess(n: int):
     return n