# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 size:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import numpy as np
f = open("input.txt", "r")
data=list()
size=22
cubes=np.zeros((size,size,size))

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [x,y,z]=[int(d) for d in line.split(',')]
    cubes[z,y,x]=1
f.close()

total_p1=0
dirs=[[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]

##############
#Part 1 
#Find total surface area, connecting cubes loses surface
for zz,faces in enumerate(cubes):
    for yy,lines in enumerate(faces):
        for xx,s in enumerate(lines):
            if s==1:
                total_p1+=6
                for direc in dirs:
                    if zz+direc[0]>=0 and zz+direc[0]<size and yy+direc[1]>=0 and yy+direc[1]<size and xx+direc[2]>=0 and xx+direc[2]<size:
                        total_p1-=int(cubes[zz+direc[0],yy+direc[1],xx+direc[2]])


####
#Part 2
#Determine only outer surface, so remove surfaces on the inside from total of p1
#Surface to be removed is the surface off all trapped volumes
##Find trapped volumes, 
outsides=np.zeros((size,size,size)) #3=part of structure 2=trapped, 1=not trapped , 0 not processed         
for zz,faces in enumerate(cubes):
    for yy,lines in enumerate(faces):
        for xx,s in enumerate(lines):
            if s==1:
                outsides[zz,yy,xx]=3  #part of structure
                continue

            cube_visited=np.zeros((size,size,size))
            cube_visited[zz,yy,xx]=1
            
            heap=[[zz,yy,xx]]
            i=0

            outsides[zz,yy,xx]=2
            #BFS quickly discovers a neightbour that should have finished it's evaluation
            while i<len(heap):
                cz=heap[i][0]
                cy=heap[i][1]
                cx=heap[i][2]
                
                #Found something previously determined to be outside
                if outsides[cz,cy,cx]==1:
                    outsides[zz,yy,xx]=1 #not trapped
                    break
                
                #Found a volume previously determined to be trapped, other than starting position
                if outsides[cz,cy,cx]==2 and not (cz==zz and cy==yy and cx==xx):
                    break #trapped
                
                #Reached a point at the edge of the volume, so can reach outside
                if cz==size-1 or cy==size-1 or cx==size-1 or cz==0 or cy==0 or cx==0:
                    outsides[zz,yy,xx]=1
                    break #not trapped
                    
                ######
                #Open paths in new, unvisited, directions
                for direc in dirs:
                    if cubes[cz+direc[0],cy+direc[1],cx+direc[2]]==0: #No cube at searching position
                        if cube_visited[cz+direc[0],cy+direc[1],cx+direc[2]]==0:
                            cube_visited[cz+direc[0],cy+direc[1],cx+direc[2]]=1
                            heap.append([cz+direc[0],cy+direc[1],cx+direc[2]])
                i+=1

#Find the surface of all trapped volumes
#Neighbourly trapped cubes causes lose of total surface
total_inner=0                    
for zz,faces in enumerate(outsides):
    for yy,lines in enumerate(faces):
        for xx,s in enumerate(lines):                
          if s==2: #trapped
              total_inner+=6
              for direc in dirs:
                  if outsides[zz+direc[0],yy+direc[1],xx+direc[2]]==2: #If neightbour is also trapped volume, dont count this surface
                      total_inner-=1

print("Part 1",total_p1)
print("Part 2",total_p1-total_inner)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))