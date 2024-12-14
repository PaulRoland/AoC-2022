# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
from collections import deque
import time
import math
start_time = time.time_ns()
import matplotlib.pyplot as plt
findn =1000000000000

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    instr=deque(line)
f.close()

#Load the tetris shapes
f = open("shapes.txt", "r")
shapes=list()
cur_shape=list()
for i,line in enumerate(f):
    if line=='\n':
        shapes.append(cur_shape)
        cur_shape=list()
        continue
    cur_shape.append(line.replace('\n',''))
f.close()
shapes.append(cur_shape)


shapes_points=list()
for cur_shape in shapes:    
    points=list()
    for row,line in enumerate(cur_shape):
        for col,s in enumerate(line):
            if s=='#':
                points.append([row,col])
    shapes_points.append(points)
                
twidth=7
tetrismap=[[0 for d in range(0,twidth)] for d in range(0,800000)]
tetrismax=[-1,-1,-1,-1,-1,-1,-1]
height=list()

loop_length=math.lcm(len(instr),len(shapes))

instr_counter=-1
stone_counter=0
prev_count=0
prev_stones=0
for i in range(0,5100):
    cur_shape=shapes_points[i%len(shapes)]
    falling=True
    cur_x=2
    cur_y=max(tetrismax)+4+max([dr for [dr,dc] in cur_shape])
    

        
    while falling:
        #print(cur_y)
        #Volgende instructie, zet deze weer achteraan
        cur_instr=instr.popleft()
        instr.append(cur_instr) 
        instr_counter+=1
        if instr_counter%(1*len(instr))==0 and len(height)>0:
            print(stone_counter,height[-1]-prev_count,stone_counter-prev_stones)
            loop_length=stone_counter-prev_stones
            loop_start=stone_counter
            loop_height=height[-1]-prev_count
            prev_count=height[-1]
            prev_stones=stone_counter
        
        #print(cur_instr)
        
        #Doe eerst de verplaatsing
        if cur_instr=='>': try_x=cur_x+1
        if cur_instr=='<': try_x=cur_x-1
        #Controleer de verplaatsing
        move=True
        for [dr,dc] in cur_shape:
            if try_x+dc<0 or try_x+dc>twidth-1:
                #print("tegen muur")
                move=False
                break
            if tetrismap[cur_y-dr][try_x+dc]==1:
                #print("hier zit al een blokje",cur_y-row,try_x+dc)
                move=False
                break
            
        if move==True:
            #print("blokje verplaatst")            
            cur_x=try_x
                    
        #Doe dan de val
        #Kan dat niet dan falling=False
        for [dr,dc] in cur_shape:
            #print(tetrismap[cur_x+dc],[cur_y-dr-1],[(cur_y-dr-1)] in tetrismap[cur_x+dc])
            if cur_y-dr-1<0:
                falling=False
                break
            if tetrismap[cur_y-dr-1][cur_x+dc]==1:
                falling=False
            
        if falling==True:
            cur_y-=1
        else:
            #Vallen is gestopt voeg vorm toe
            #print("vallen is gestopt!")
            stone_counter+=1
            for [dr,dc] in cur_shape:
                tetrismap[cur_y-dr][cur_x+dc]=1
                if cur_y-dr>tetrismax[cur_x+dc]:
                    tetrismax[cur_x+dc]=cur_y-dr
            #print(tetrismap)
    height.append(max(tetrismax)+1)

#Repereterend patroon van blokjes en instructies elke 
poss_index=((findn-loop_start)%loop_length)+loop_start
total_p2=height[poss_index]+loop_height*(findn-poss_index)/loop_length



#    print(b-a)
#plt.plot(height)    
#print(loop_length,hoogte_loop)
print("Part 1",height[2021])
print("Part 2",total_p2-1)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))