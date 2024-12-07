# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import bisect
start_time = time.time_ns()

data=list()

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(line.split(' -> '))
    
f.close()

grid=[ [] for n in range(0,500)]
map_cf=[ [] for n in range(0,999)]

max_y=0
for instructions in data:
    for instr1,instr2 in zip(instructions,instructions[1:]):
        instr1=[int(d) for d in instr1.split(',')]
        instr2=[int(d) for d in instr2.split(',')]
        if instr1[0]==instr2[0]: #kolommen zijn hetzelfde
            for row in range(min(instr1[1],instr2[1]),max(instr1[1],instr2[1])+1):
                grid[row].append(instr1[0])
                map_cf[instr1[0]].append(row)
            if row>max_y:
                max_y=row
        else: #rijenn zijn hetzelfde
            for col in range(min(instr1[0],instr2[0]),max(instr1[0],instr2[0])+1):
                grid[instr1[1]].append(col)
                map_cf[col].append(instr1[1])

sand_start=[0,500] #row col

void=max_y+2

for i,line in enumerate(grid):
    data=list(set(line))
    data.sort()
    grid[i]=list(set(line))
    
for i,line in enumerate(map_cf):
    data=list(set(line))
    data.sort()
    data.append(void)
    map_cf[i]=data
    

in_void=False #Conditie p1
tot_top=False #Coditie p2

sand_used=0
total_p1=0
total_p2=0

while tot_top==False:
    
    #Beginplek zand
    nrow=sand_start[0]
    ncol=sand_start[1]
    falling=True
    
    while falling:
        #print(nrow,ncol)
        #Volgende plek beschikbaar, direct beneden
        ind=bisect.bisect_right(map_cf[ncol],nrow)
        nrow=map_cf[ncol][ind]-1
        
        if nrow>max_y and in_void==False: #Conditie voor part 1
            total_p1=sand_used
            in_void=True
            
        #check stability left down
        if nrow+1 not in map_cf[ncol-1]: #If place is empty continue falling from here
            ncol-=1
            nrow+=1
            continue #Ga weer terug naar het begin van de loop en val verder
        elif nrow+1 not in map_cf[ncol+1]: #If place is empty continue falling from here
            ncol+=1
            nrow+=1
            continue
        else:
            #stable position
            sand_used+=1
            bisect.insort_left(map_cf[ncol],nrow)
            falling=False
            
            if nrow==0 and ncol==500: #Eindconditie voor part 2
                total_p2=sand_used
                tot_top=True
                break

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))