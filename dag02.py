# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
start_time = time.time_ns()

f = open("input.txt", "r")


total_score=0
total_score2=0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [opp,own]=line.split(' ')
    print(line)
    
    game_value=3
    new_hand=0
    if own=='X':
        if opp=='B':
            game_value=0
            new_hand='X'
        if opp=='C':
            game_value=6
            new_hand='Y'
        if opp=='A':
            new_hand='Z'
            
    if own=='Y':
        new_hand=chr(ord(opp)+23) #Match opponent
        if opp=='A':
            game_value=6            
        if opp=='C':
            game_value=0
            
    if own=='Z':
        if opp=='A':
            game_value=0
            new_hand='Y'
        if opp=='B':
            game_value=6
            new_hand='Z'
        if opp=='C':
            new_hand='X'
            
    #A: 65, B: 66, C:66
    total_score+=game_value+ord(own)-87
    total_score2+=ord(new_hand)-87+3*(ord(own)-88)
    
    
f.close()









print("Part 1",total_score)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
print("Part 2",total_score2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))