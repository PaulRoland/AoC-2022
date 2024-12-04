# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()

def visible(numbers):
    #Check if it is higher than all other trees upto the edge
    return numbers[-1]>np.max(numbers[:-1])    


def scenic(numbers):

    multiplier=1
    for check in numbers:
        
        #Find the first tree that is higher/as high
        a= np.where(check[1:] >= check[0])
        if len(a[0])>0:
            multiplier=multiplier*(a[0][0]+1)
        #None found, it can see to the edge
        else:
            multiplier=multiplier*(len(check)-1)
    return multiplier

f = open("input.txt", "r")
size = 99
grid = np.zeros((size,size),dtype=int)
for i,line in enumerate(f):
    line=line.replace('\n','')
    for j,s in enumerate(line):
        grid[i,j]=int(s)
f.close()

teller=0
scenic_score=0

for i in range(1,size-1):
    for j in range(1,size-1):
        scenic_score=max(scenic_score,scenic([grid[0:i+1,j][::-1],grid[i,0:j+1][::-1],grid[i:,j],grid[i,j:]]))
        if visible(grid[0:i+1,j]) or visible(grid[i,0:j+1]) or visible(grid[i:,j][::-1]) or visible(grid[i,j:][::-1]):
            teller+=1
            continue

print("Part 1",teller+4*size-4)
print("Part 2",scenic_score)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))