# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
start_time = time.time_ns()

def cont_over(range1,range2):
    numbers1=list(range(int(range1.split('-')[0]),int(range1.split('-')[1])+1))
    numbers2=list(range(int(range2.split('-')[0]),int(range2.split('-')[1])+1))
    
    has_overlap = len(set(numbers1).intersection(set(numbers2)))>0
    
    if set(numbers1)<=set(numbers2):
        return [1,has_overlap]
    if set(numbers2)<=set(numbers1):
        return [1,has_overlap]
    return [0,has_overlap]


f = open("input.txt", "r")
total1=0
total2=0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [range1,range2]=line.split(',')
    
    [contains,overlap]=cont_over(range1,range2)
    total1+=contains
    total2+=overlap
f.close()









print("Part 1",total1)
print("Part 2",total2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))