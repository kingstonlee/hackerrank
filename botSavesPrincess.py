#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/saveprincess
'''

def findCurrentPosition(grid):
    position_id = 'm'
    for index, value in enumerate(grid):
        if position_id in value:
            subindex = value.index(position_id)
            break
    return [index, subindex]

def findPrincessPosition(grid):
    position_id = 'p'
    for index, value in enumerate(grid):
        if position_id in value:
            subindex = value.index(position_id)
            break
    return [index, subindex]

def displayPathtoPrincess(n,grid):
    moves = []
    current_position = findCurrentPosition(grid)
    princess_position = findPrincessPosition(grid)
    x = current_position[0] - princess_position[0]
    y = current_position[1] - princess_position[1]
    
    #TODO: Not the correct way of adding multiples to a list
    if x < 0:
        moves.append('RIGHT' * abs(x))
    elif x > 0:
        moves.append('LEFT' * abs(x))
    if y < 0:
        moves.append('DOWN' * abs(y))
    elif y > 0:
        moves.append('UP' * abs(y))
    
    for move in moves:
        print(move)
    
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
