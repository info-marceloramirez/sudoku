# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:18:48 2020

@author: Marcelo Ramirez

-------------
Sudoku Solver
-------------

"""

import numpy as np

grid0 = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,1,9]]

grid = [[3,0,4,5,9,0,0,0,6],
        [0,1,0,0,0,8,5,0,0],
        [0,7,5,0,0,0,8,0,2],
        [1,5,0,0,0,0,0,0,4],
        [0,0,0,0,2,9,0,0,3],
        [0,4,3,0,5,1,0,7,8],
        [0,0,6,0,0,0,0,8,7],
        [0,0,7,0,0,6,0,0,0],
        [0,9,0,7,0,3,0,2,0]]

def possible(bo,y,x,n):

    #Check row
    for i in range(0,9):
        if bo[y][i] == n:
            return False
        
    #Check column    
    for i in range(0,9):
        if bo[i][x] == n:
            return False
        
    #Check box
    x0 = (x//3)*3
    y0 = (y//3)*3
    
    for i in range(0,3):
        for j in range(0,3):
            if bo[y0 + i][x0 + j] == n:
                return False
    return True

def solve(bo):
    
    for y in range(9):
        for x in range(9):
            if bo[y][x] == 0:
                for n in range(1,10):
                    if possible(bo,y,x,n):
                        bo[y][x] = n
                        solve(bo)
                        bo[y][x] = 0
                return
    print(np.matrix(bo))

print(np.matrix(grid))
print('*********************')

solve(grid)
