# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()


def give_col(test_r,test_c):
    if test_c>wrap_rows[test_r][1]:
        return wrap_rows[test_r][0]
    
    if test_c<wrap_rows[test_r][0]:
        return wrap_rows[test_r][1]
    return test_c

def give_row(test_r,col):
    if test_r>wrap_cols[col][1]:
        return wrap_cols[col][0]
    
    if test_r<wrap_cols[col][0]:
        return wrap_cols[col][1]
    return test_r


def give_rowcol3d(test_r,test_c,dircount):
    global size
    if dircount==0:
        if test_c>wrap_rows[test_r][1]:
            if test_r>=0 and test_r<size:
                #Loop van 2 rechts eraf naar rechterkant 4
                test_r = size*3-1-test_r #12-1-0 -> 0 naar 11
                test_c = wrap_rows[test_r][1]
                dircount=2
                #print("moeilijke kubus 1, 2-4")
                return [test_r,test_c,dircount]
            
            if test_r>=size and test_r<2*size:
                #Loop van 3 rechts eraf naar onderkant 2
                test_c=test_r+size
                test_r=wrap_cols[test_c][1]
                dircount=3
                #print("moeilijke kubus 2, 3-2")
                return [test_r,test_c,dircount]
                
            if test_r>=2*size and test_r<3*size:
                #Loop van 4 rechts eraf naar rechterkant 2
                test_r = size*3-1-test_r #12-1-11 -> 11 naar 0
                test_c = wrap_rows[test_r][1]
                dircount=2
                #print("moeilijke kubus 3, 4-2")
                return [test_r,test_c,dircount]
                
            if test_r>=3*size and test_r<4*size:
                #Loop van 6 rechts eraf naar onderkant 4
                test_c=test_r-2*size
                test_r = wrap_cols[test_c][1]
                dircount=3
                #print("moeilijke kubus 4, 6-4")
                return [test_r,test_c,dircount]
            
    elif dircount==2:
        if test_c<wrap_rows[test_r][0]:
        
            if test_r>=0 and test_r<size:
                #Loop van 1 links eraf naar linkerkant 5
                test_r=3*size-1-test_r
                test_c=wrap_rows[test_r][0]
                dircount=0
                #print("moeilijke kubus 5, 1->5")
                return [test_r,test_c,dircount]
            
            if test_r>=size and test_r<2*size:
                #Loop van 3 links eraf naar bovenkant 5
                test_c=test_r-size
                test_r=wrap_cols[test_c][0]
                dircount=1
                #print("moeilijke kubus 6, 3-5")
                return [test_r,test_c,dircount]
                
            if test_r>=2*size and test_r<3*size:
                #loop van 5 links eraf naar linkerkant 1
                test_r=3*size-test_r-1
                test_c=wrap_rows[test_r][0]
                dircount=0
                #print("moeilijke kubus 7, 5-1")
                return [test_r,test_c,dircount]
                
            if test_r>=3*size and test_r<4*size:
                #Loop van 6 links eraf naar bovenkant 1
                test_c=test_r-2*size
                test_r=wrap_cols[test_c][0]
                dircount=1
                #print("moeilijke kubus 8, 6-1")
                return [test_r,test_c,dircount]
            
    elif dircount==3:
        if test_r<wrap_cols[test_c][0]:
            #Loop van 5 boven naar links 3
            if test_c>=0 and test_c<size:
                test_r=size+test_c
                test_c=wrap_rows[test_r][0]
                dircount=0
                #print("moeilijke kubus 9, 5-3")
                return [test_r,test_c,dircount]
                
            if test_c>=size and test_c<2*size:
                #Loop van 1 boven naar links 6
                test_r=test_c+2*size
                test_c=wrap_rows[test_r][0]
                dircount=0
                #print("moeilijke kubus 10,1-6")
                return [test_r,test_c,dircount]
            
            if test_c>=2*size and test_c<3*size:
                #Loop van 2 boven naar onderkant 6
                test_c=test_c-size*2
                test_r=wrap_cols[test_c][1]
                dircount=3
                #print("moeilijke kubus 11, 2-6")
                return [test_r,test_c,dircount]
    elif dircount==1:         
        if test_r>wrap_cols[test_c][1]:
        #Loop van 6 onder naar 2 boven
            if test_c>=0 and test_c<size:
                test_c=2*size+test_c
                test_r=wrap_cols[test_c][0]
                dircount=1
                #print("moeilijke kubus 12, 6-2" )
                return [test_r,test_c,dircount]
                
            if test_c>=size and test_c<2*size:
                #Loop van 4 onder naar rechts 6
                test_r=test_c+2*size
                test_c=wrap_rows[test_r][1]
                dircount=2
                #print("moeilijke kubus 13, 4-6")
                return [test_r,test_c,dircount]
            
            if test_c>=2*size and test_c<3*size:
                #Loop van 2 onder naar rechts 3
                test_r=test_c-size
                test_c=wrap_rows[test_r][1]
                dircount=2
                #print("moeilijke kubus 14, 2-3")
                return [test_r,test_c,dircount]
        
    return [test_r,test_c,dircount]


f = open("input.txt", "r")
instruction=False
data=list()
size=50
for i,line in enumerate(f):
    
    if line=='\n':
        instruction=True
        continue
    
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    #print(line)
    if instruction==True:
        line=line.replace('L',' L ').replace('R',' R ')
        instructions=line.split(' ')
    else:
        data.append(line)
f.close()


wrap_rows=list()
for line in data:
    a=re.findall(r'[ ]*',line)
    #print(len(a[0]))
    wrap_rows.append([len(a[0]),len(line)-1])


wrap_cols_temp=[ [] for d in range(0,len(data[9]))]
for r,line in enumerate(data):
    for c,s in enumerate(line):
        if s=='.' or s=='#':
            wrap_cols_temp[c].append(r)

wrap_cols=[ [] for d in range(0,len(data[9]))]
for c,col in enumerate(wrap_cols_temp):
    wrap_cols[c] = [min(col),max(col)]



##### Part 1
#starting position
cr=0
cc=wrap_rows[0][0]+0

dirs= [[0,1],[1,0],[0,-1],[-1,0]] #dr,dc
dircount=0

for instr in instructions:
    if instr=='R':
        dircount=(dircount+1)%4
        continue
    if instr=='L':
        dircount=(dircount-1)%4
        continue
    
    nsteps=int(instr)
    direction = dirs[dircount]
    for step in range(0,nsteps):
        
        if dircount==0 or dircount==2: #going in a row
            test_r=cr
            test_c=give_col(test_r,cc+direction[1])
            
        if dircount==1 or dircount==3: #going in a col
            test_c=cc
            test_r=give_row(cr+direction[0],test_c)
        
        if data[test_r][test_c]=='.':
            cr=test_r
            cc=test_c
        else:
            break
total_p1=1000*(cr+1)+4*(cc+1)+dircount


###Part 2
cr=20
cc=wrap_rows[0][0]+size+20

dirs= [[0,1],[1,0],[0,-1],[-1,0]] #dr,dc
dircount=0

for instr in instructions:
    if instr=='R':
        dircount=(dircount+1)%4
        #print(cr,cc,dircount)
        continue
    if instr=='L':
        dircount=(dircount-1)%4
        #print(cr,cc,dircount)
        continue
    
    nsteps=int(instr)
    direction = dirs[dircount]
    for step in range(0,nsteps):
        direction = dirs[dircount] #direction kan aanpassen door de kubus
        
        [test_r,test_c,test_dircount]=give_rowcol3d(cr+direction[0],cc+direction[1],dircount)
        
        #print(cr,cc,dircount, 'to', test_r,test_c,test_dircount)
        if data[test_r][test_c]=='.':
            cr=test_r
            cc=test_c
            dircount=test_dircount
        else:
            break
total_p2=1000*(cr+1)+4*(cc+1)+dircount

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))