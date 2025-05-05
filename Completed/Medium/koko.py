from typing import List
def minEatingSpeed(piles: List[int], h: int):
    low,high = 1,max(piles)

    while low <= high:
        time = 0
        k = (high-low)//2 +low
        time = sum([-(i//-k) for i in piles])

        if time > h:
            low = k+1
        if time <=h:
            high = k-1
    return low

print(minEatingSpeed(piles=[30,11,23,4,20],h=6))