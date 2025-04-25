#704. Binary Search
#Difficulty: Easy
from typing import List
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums: List[int], target: int) -> int:
    low,high = 0,len(nums) -1

    while low <= high:
        mid = low + (high-low) //2
      
        if nums[mid] == target:
            return mid  
        
        if nums[mid] > target:
            high = mid - 1 

        if nums[mid] < target:
            low = mid + 1
    return -1
            
print(search([-1,0,3,5,9,12],9))

# Ignore this section

# def solve(direction, x, y, width, height):
#     if not hasattr(solve, "left"):
#         solve.left = 0
#         solve.right = width - 1
#         solve.top = 0
#         solve.bottom = height - 1

#     if "U" in direction:
#         solve.bottom = min(solve.bottom, y - 1)
#     if "D" in direction:
#         solve.top = max(solve.top, y + 1)
#     if "L" in direction:
#         solve.right = min(solve.right, x - 1)
#     if "R" in direction:
#         solve.left = max(solve.left, x + 1)


#     box_width = solve.right - solve.left + 1
#     box_height = solve.bottom - solve.top + 1

#     if box_width <= 3 and box_height <= 3:
#         dx_map = {
#             "U": 0, "UR": 1, "R": 1, "DR": 1,
#             "D": 0, "DL": -1, "L": -1, "UL": -1
#         }
#         dy_map = {
#             "U": -1, "UR": -1, "R": 0, "DR": 1,
#             "D": 1, "DL": 1, "L": 0, "UL": -1
#         }

#         dx = dx_map[direction]
#         dy = dy_map[direction]

#         steps_x = (solve.right - x) if dx > 0 else (x - solve.left if dx < 0 else float('inf'))
#         steps_y = (solve.bottom - y) if dy > 0 else (y - solve.top if dy < 0 else float('inf'))
#         max_steps = min(steps_x if dx != 0 else float('inf'),
#                         steps_y if dy != 0 else float('inf'))

#         final_x = x + dx * max_steps
#         final_y = y + dy * max_steps
#         return [final_x, final_y]
    
#     next_x = (solve.left + solve.right) // 2
#     next_y = (solve.top + solve.bottom) // 2
#     return [next_x, next_y]