from typing import List
# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#     res = [elem for row in matrix for elem in row]
#     high = len(res)-1
#     low = 0
#     res.sort()
#     while low <= high:
#             mid = (high-low)//2 +low
#             if res[mid] == target:
#                 return True
#             if res[mid] > target:
#                 high = mid -1
#             if res[mid] < target:
#                 low = mid+1
#     return False

def searchMatrixII( matrix: List[List[int]], target: int):
    for row in matrix:
        low = 0
        high = len(row)-1

        while low<=high:
            mid = (high-low)//2 +low
            if row[mid] == target:
                return True
            if  row[mid] > target:
                high = mid-1
            if  row[mid] < target:
                low = mid+1
    return False
print(searchMatrixII(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target=5))