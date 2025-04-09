from typing import List
def maximalSquare(matrix: List[List[str]]) -> int:
    highest =0
    for row in range(len(matrix)-1):
        for col in range(len(matrix[row])-1):
            sub = matrix[row][col:col+2] + matrix[row+1][col:col+2]
            res = [int(i) for i in sub]
            highest = max(highest,sum(res))
            print(res)
    return highest
print(maximalSquare(matrix = [
    ["0","1"],["1","0"]]))