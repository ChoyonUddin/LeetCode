def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    res = [elem for row in matrix for elem in row]
    high = len(res)-1
    low = 0
    while low <= high:
            mid = (high-low)//2 +low
            if res[mid] == target:
                return True
            if res[mid] > target:
                high = mid -1
            if res[mid] < target:
                low = mid+1
    return False