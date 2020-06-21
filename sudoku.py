# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:09:17 2020

@author: Marcelo Ramirez

-------------
Sudoku Solver
-------------

"""

#import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

#print(np.matrix(grid))

#def possible(y,x,n):
#    global grid
#    for i in range(0,9):
#        if grid[y][i] == n:
#            return False
#    for i in range(0,9):
#        if grid[x][i] == n:
#            return False
#    x0 = (x//3)*3
#    y0 = (y//3)*3
#    for i in range(0,3):
#        for j in range(0,3):
#            if grid[y0+i][x0+j] == n:
#                return False
#    return True
#
#def solve():
#    global grid
#    for y in range(9):
#        for x in range(9):
#            if grid[y][x] == 0:
#                for n in range(1,10):
#                    if possible(y,x,n):
#                        grid[y][x] = n
#                        solve()
#                        grid[y][x] = 0
#    print(np.matrix(grid))
#
##    input('More?')
#
#solve()

def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range (1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
            
    return False

def valid(bo, num, pos):
    
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and [i,j] != pos:
                return False
            
    return True        

def print_board(bo):
    
    for i in range(len(bo)):
        if i%3 == 0 and i != 0:
            print('-------------------')
            
        for j in range(len(bo[0])):
            if j%3 == 0 and j != 0:
                print('|', end = '')
                
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end = '')
    

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i,j) #(row,column)
    return None
                
print_board(grid)
solve(grid)
print('*******************')     
print_board(grid)

    
        

