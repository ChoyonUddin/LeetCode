#397. Integer Replacement
#Difficulty: Medium

#Description: Given a positive integer n, you can apply one of the following operations:

# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.

#Return the minimum number of operations needed for n to become 1.

#Progress: Under Development 

#Notes:

def integerReplacement(n: int) -> int:
    '''
    if n % 2 == 1 and n != 1:
        counter += 1
        return integerReplacement(n-1)
    if n % 2 == 0:
        counter += 1
        return integerReplacement(n//2)
    '''
    counter = 0
    return counter
print(integerReplacement(8))