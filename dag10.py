# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

cycle = 0
reg_x=1
signal_strength=0
f = open("input.txt", "r")
cycle_set={20,60,100,140,180,220}
screen=[' ']*240
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    if 'noop' in line:
        during_cycle={cycle+1}
        add_cycle=1
        add_reg_x=0

    if 'addx' in line:
        add_cycle=2
        add_reg_x=int(line[4:])
        during_cycle={cycle+1,cycle+2}
        
    if during_cycle.intersection(cycle_set):
        for a in during_cycle.intersection(cycle_set):
            signal_strength+=int(a)*reg_x
            #print(a,'*',reg_x,int(a)*reg_x)
    
    for c in during_cycle:
        #print(c,reg_x-1,reg_x+1)
        a=int(c)-1
        if a%40==reg_x or a%40==reg_x-1 or a%40==reg_x+1:
            screen[a]='#'
        
    cycle+=add_cycle
    reg_x+=add_reg_x
    
f.close()

print("Part 1:",signal_strength)
print("Part 2:")
print(''.join(screen[:40]))
print(''.join(screen[40:80]))
print(''.join(screen[80:120]))
print(''.join(screen[120:160]))
print(''.join(screen[160:200]))
print(''.join(screen[200:240]))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))