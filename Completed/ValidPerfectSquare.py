'''
Difficulty: Easy
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Status: Completed

Notes: Probably a better way to do this
'''
def isPerfectSquare(num: int) -> bool:
        return num**0.5 == round(num**0.5)