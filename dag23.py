# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

elf_loc=list()
elf_dict=dict()
i=0
f = open("input.txt", "r")
p1_steps=10
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s=='#':
            key=str(row)+','+str(col)
            elf_loc.append([row,col])
            elf_dict.update({key:i})
            i+=1
f.close()

directions = [[-1,0],[0,1],[1,0],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]

move_dir= [
    [[-1,-1],[-1,0],[-1,1],[-1,0]],
    [[1,-1],[1,0],[1,1],[1,0]],
    [[-1,-1],[0,-1],[1,-1],[0,-1]],
    [[-1,1],[0,1],[1,1],[0,1]]]


step=0

while True:
    step+=1
    if step%1000==0:
        print(step)
    new_elf_loc=list()
    for [cr,cc] in elf_loc:    
        #check eight surroundings
        moving=False
        for [dr,dc] in directions:
            key=str(cr+dr)+','+str(cc+dc)
            if key in elf_dict:
                moving=True
        
        #Iets in de buurt    
        if moving==True:
            for dir1,dir2,dir3,move in move_dir:
                
                key1=str(cr+dir1[0])+','+str(cc+dir1[1])
                key2=str(cr+dir2[0])+','+str(cc+dir2[1])
                key3=str(cr+dir3[0])+','+str(cc+dir3[1])
                
                if key1 in elf_dict or key2 in elf_dict or key3 in elf_dict:
                    continue
                #Hier komen we als alle keys er niet in staan, dus is het een vrije plek, dus zijn we klaar
                cr+=move[0]
                cc+=move[1]
                break
        new_elf_loc.append([cr,cc])
        
    new_elf_dict=dict()
    keys_to_delete=list()
    for i,[row,col] in enumerate(new_elf_loc):
        key=str(row)+','+str(col)
        
        #Kijk of hier al een elf staat, dan beide terugzetten
        if key in new_elf_dict:
            i2=new_elf_dict[key]
            [r1,c1]=elf_loc[i]
            [r2,c2]=elf_loc[i2]
            new_elf_loc[i]=[r1,c1]
            
            
            key1=str(r1)+','+str(c1)    
            key2=str(r2)+','+str(c2)    
            
            new_elf_loc[i]=[r1,c1]
            new_elf_loc[i2]=[r2,c2]
            
            new_elf_dict.update({key1:i})
            new_elf_dict.update({key2:i2})
        
            keys_to_delete.append(key)
        else:
            new_elf_dict.update({key:i})
    
    for key in keys_to_delete:
        del new_elf_dict[key]
        
    
    if elf_dict==new_elf_dict:
        break
        
    move_dir2=list(move_dir)
    move_dir=move_dir2[1:]
    move_dir.append(move_dir2[0])

    elf_dict=dict(new_elf_dict)
    elf_loc=list(new_elf_loc)
    
    
    if step==p1_steps:
        min_r=1000
        max_r=0
        min_c=1000
        max_c=0
        for [r,c] in elf_loc:
            max_r=max(max_r,r)
            min_r=min(min_r,r)
            max_c=max(max_c,c)
            min_c=min(min_c,c)
        rectangle = (max_r-min_r+1)*(max_c-min_c+1)
        

min_r=1000
max_r=0
min_c=1000
max_c=0
for [r,c] in elf_loc:
    max_r=max(max_r,r)
    min_r=min(min_r,r)
    max_c=max(max_c,c)
    min_c=min(min_c,c)    

print("== End of Round",step,"==")
for r in range(min_r,max_r+1):
    string=''
    for c in range(min_c,max_c+1):
        if [r,c] in elf_loc:
            string+='X'
        else:
            string+=' '
    print(string)
print() 
 
    
    
    
        



print("Part 1",rectangle-len(elf_loc))
print("Part 2",step)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))