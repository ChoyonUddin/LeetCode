'''
Container With Most Water
Solved 
You are given an integer array heights where heights[i] represents the height of the ith bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
'''
from typing import List
def maxArea(self, heights: List[int]) -> int:
    l,r = 0, len(heights)-1
    largest = 0
    while l<r:
        x = abs(r-l)
        largest = max(largest,x*min(heights[l],heights[r]))
        print(f'Largest: {largest}, l:{l}, r:{r}, x:{x}')
        if heights[l]<heights[r]:
            l+=1
        elif heights[r]<heights[l]:
            r-=1
        elif heights[l]==heights[r]:
            l+=1
    return largest