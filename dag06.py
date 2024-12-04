# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
a=0
b=0

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for j in range(3,len(line)):
        if len(set(line[j-3:j+1])) == 4:
           a=j+1
           break
 
    for j in range(13,len(line)):
        if len(set(line[j-13:j+1])) == 14:
           b=j+1
           break
f.close()



print("Part 1",a)
print("Part 2",b)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))