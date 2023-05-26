#Choyon Uddin 
#June 27th 2022
#Sudoku Solver

#Imports
import numpy as np

def printBoard(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
        
def solve(grid,col,row,num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    
def sudoku(grid,col,row):

#0s mean that no value is in that cell
board = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]
printBoard(board)