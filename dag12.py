# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()


def kortste_pad(node,total,end_node,visited_list):
    if total < dist[node]:
        dist[node]=total #kortste pad mogelijk om tot hier te komen
    else:
        return
    
    if node==end_node:
        print("nieuwe beste",total)
        return
    
    #Open nieuwe vertakkingen, kijk of we niet al op de nieuwe node zijn geweest, want dan gaat het anders lang duren
    for new_node in graph[node]:
        if new_node not in visited_list:
            new_visited = list(visited_list) #Rare python list memory geheugen shit
            new_visited.append(new_node)
            kortste_pad(new_node,total+1,end_node,new_visited)


def kortste_pad2(node,total,end_value,visited_list):
    global beste
    if total>beste:
        return
    
    if total < dist2[node]:
        dist2[node]=total #kortste pad mogelijk om tot hier te komen
    else:
        return
    
    [row,col]=[int(d) for d in node.split('_')]
    if grid[row,col]==end_value:
        beste=total
        print("nieuwe beste",total)
        print(visited_list)
        return
    
    #Open nieuwe vertakkingen, kijk of we niet al op de nieuwe node zijn geweest, want dan gaat het anders lang duren
    for new_node in graph2[node]:
        if new_node not in visited_list:
            new_visited = list(visited_list) #Rare python list memory geheugen shit
            new_visited.append(new_node)
            kortste_pad2(new_node,total+1,end_value,new_visited)
        

data=list()
f = open("input.txt", "r")
for line in f:
    line=line.replace('\n','')
    data.append(line)
f.close()

grid=np.ones((len(data)+2,len(data[0])+2))*999

start_r=0
start_c=0
end_r=0
end_c=0

#create a maze with padding of 1
for row,line in enumerate(data):
    for col,ltr in enumerate(line):
        if ltr=='S':
            start_r=row+1
            start_c=col+1
            grid[row+1,col+1]=ord('a')
        elif ltr=='E':
            end_r=row+1
            end_c=col+1
            grid[row+1,col+1]=ord('z')
        else:
            grid[row+1,col+1]=ord(ltr)


#create a graph from the maze
graph=dict()
graph2=dict()
dist=dict()
dist2=dict()
for row,line in enumerate(grid):
    for col,v in enumerate(line):
        if v==999: #dont check the borders
            continue
        key=str(row)+'_'+str(col)
        
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        for direc in dirs:
            if grid[row+direc[0],col+direc[1]]-v<=1: #Look up/down Height difference of maximum one
                new_key=str(row+direc[0])+'_'+str(col+direc[1])
                if key in graph:
                    graph[key].append(new_key)
                else:
                    graph.update({key:[new_key]})
                    dist.update({key:9999})
                    
            if grid[row+direc[0],col+direc[1]]-v>=-1 and grid[row+direc[0],col+direc[1]]-v<50: #make graph also in other direction
                new_key=str(row+direc[0])+'_'+str(col+direc[1])
                if key in graph2:
                    graph2[key].append(new_key)
                else:
                    graph2.update({key:[new_key]})
                    dist2.update({key:9999}) 

#solve the shortest distance on the graph
start_key=str(start_r)+'_'+str(start_c)
end_key=str(end_r)+'_'+str(end_c)


#kortste_pad(start_key,0,end_key,[start_key])
beste=dist[end_key]
kortste_pad2(end_key,0,ord('a'),[end_key])

print("Part 1",dist[end_key])
print("Part 2",beste)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))