from typing import List
def minEatingSpeed(piles: List[int], h: int):
    k = 0
    high = max(piles)
    low = 1

    while low <= high:
        k = (-(high-low)//2)*-1 + low
        arr = [(i//-k)*-1 for i in piles]
        print(k)
        res = sum(arr)
        if res == h:
            return k
        if res > h:
            low = k+1
        if res < h:
            high = k-1
    return k
print(minEatingSpeed(piles=[30,11,23,4,20],h=9))