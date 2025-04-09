from typing import List
def hasDuplicate(nums: List[int]) -> bool:
        res = set(nums)
        print(res)
        if len(nums) == len(res):
            return True
        return False
print(hasDuplicate([1, 2, 3, 4]))