# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()

f = open("input.txt", "r")
blz=list() #blizzards

blz_dir={'>':[0,1],'<':[0,-1],'^':[-1,0],'v':[1,0]}
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    
    for col,s in enumerate(line):
        if s in blz_dir:
            blz.append([row,col,blz_dir[s]])
        if s=='#':
            blz.append([row,col,[0,0]]) #een muur is een stilstaande blizzard, soort van
    print(line)
f.close()
sr=0
sc=1
er=row
ec=col-1
nrow=row+1
ncol=col+1


walk_dirs=[[1,0],[0,1],[0,-1],[-1,0],[0,0]]
#Start and end locations
sr_l=[sr,er,sr]
sc_l=[sc,ec,sc]
er_l=[er,sr,er]
ec_l=[ec,sc,ec]
best_times=list()
best_time=0
for sr,sc,er,ec in zip(sr_l,sc_l,er_l,ec_l):
          #row,column,time
    heap=[[sr,sc,best_time]]
    i=0
    grid_time=-1
    while i<len(heap):
        [cr,cc,t]=heap[i]
        i+=1
        if cr==er and cc==ec:
            #BFS, dus eerste de beste
            best_time=t
            best_times.append(best_time)
            break
        t=t+1
        
        if grid_time!=t: #Door de BFS gaan we steeds een verder in de tijd dus kunnen we de kaart opslaan
            moves=np.zeros((nrow,ncol))
            grid=np.zeros((nrow,ncol))
            for blizzard in blz:
                br = blizzard[0]+t*blizzard[2][0]
                bc = blizzard[1]+t*blizzard[2][1]
                if blizzard[2]!=[0,0]: #Muren staan stil en blijven aan de rand
                    br=1+ (br-1)%(nrow-2) #De blizzards hebben deze modulo
                    bc=1+ (bc-1)%(ncol-2)
                grid[br,bc]=1
            grid_time=t
        
        for [dr,dc] in walk_dirs:
            if cr+dr<0 or cr+dr>=nrow : #Begin-/eindsituatie afvangen, waar je van de kaart kan
                continue
            
            if grid[cr+dr,cc+dc]==0 and moves[cr+dr,cc+dc]==0:
                moves[cr+dr,cc+dc]=1
                heap.append([cr+dr,cc+dc,t])
            
print("Part 1",best_times[0])
print("Part 2",best_times[2])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))