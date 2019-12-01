#!/usr/bin/env Python
import re

SIZE = 1000
print SIZE
grid = [[0 for x in range(SIZE)] for y in range (SIZE)]

myFile = open('input.txt','r')
f = list(myFile.readlines())
print len(f)

for line in f:
    match = re.findall(r'[\d]{1,3}',line) #find all digits with 1-3 decimals
    match = map(int,match) #convert to int
    x1 = match[0]
    y1 = match[1]
    x2 = match[2]
    y2 = match[3]

    if line.startswith('turn on'):
        for row in range(x1, x2+1):
            for col in range(y1,y2+1):
                grid[row][col] = 1
    elif line.startswith('turn off'):
        for row in range (x1, x2+1):
            for col in range(y1,y2+1):
                grid[row][col] = 0
    elif line.startswith('toggle'):
        for row in range (x1, x2+1):
            for col in range(y1,y2+1):
                grid[row][col] = 1 - grid[row][col]

print sum(sum(x) for x in grid)

#print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in grid]))
