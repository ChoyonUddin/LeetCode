from typing import List
#54
#Given an m x n matrix, return all elements of the matrix in spiral order.
#difficulty: Medium
#Status: Complete
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        row,col = len(matrix),len(matrix[0])
        left,right,up,down = 0, col, 0, row

        while right>left and down>up:

            for i in range(left,right):
                res.append(matrix[up][i])
            up +=1

            for i in range(up,down):
                res.append(matrix[i][right-1])
            right -=1

            if not (right>left and down>up):
                break
                
            for i in range(right-1,left-1,-1):
                res.append(matrix[down-1][i])
            down -=1

            for i in range(down-1,up-1,-1):
                res.append(matrix[i][left])
            left +=1
            
            
        return res