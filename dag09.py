# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")

stukjes = 10
x=[0]*stukjes
y=[0]*stukjes

allowed_locs=[[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1],[-1,0],[-1,1]]
key2_dict=dict()
key9_dict=dict()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    direc=line[0]
    steps=int(line[1:])

    #move h
    for step in range(steps):

        #stukje nul volgt de instructies
        if direc=='U':
            y[0]=y[0]+1
        if direc=='D':
            y[0]=y[0]-1
        if direc=='R':
            x[0]=x[0]+1
        if direc=='L':
            x[0]=x[0]-1
            
        #de rest volgt, volgens de regels
        for stukje in range(1,stukjes):
            touching=False
            for check in allowed_locs:
                
                if y[stukje] == y[stukje-1] + check[0] and x[stukje] == x[stukje-1] + check[1]:
                    touching=True
            
            if touching==False:
                
                #niet touching maar wel in zelfde rij, dus 2 verschil in x of y  
                if x[stukje] == x[stukje-1] or y[stukje] == y[stukje-1]:
                    x[stukje]-=int((x[stukje]-x[stukje-1])/2)
                    y[stukje]-=int((y[stukje]-y[stukje-1])/2)
                else:
                    #diagonaal
                    if x[stukje-1]>x[stukje]:
                        x[stukje]=x[stukje]+1 
                    elif x[stukje-1]<x[stukje]:
                        x[stukje]=x[stukje]-1
                    if y[stukje-1]>y[stukje]:
                        y[stukje]=y[stukje]+1 
                    elif y[stukje-1]<y[stukje]:
                        y[stukje]=y[stukje]-1
     
        key9 = str(y[-1])+'_'+str(x[-1])
        key2 = str(y[1])+'_'+str(x[1])
        if key2 in key2_dict:
            key2_dict[key2]=key2_dict[key2]+1
        else:
            key2_dict.update({key2:1})
        if key9 in key9_dict:
            key9_dict[key9]=key9_dict[key9]+1
        else:
            key9_dict.update({key9:1})
f.close()



print("Part 1",len(key2_dict.keys()))
print("Part 2",len(key9_dict.keys()))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))