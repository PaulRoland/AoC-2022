# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()


f = open("input.txt", "r")

crates = ['']*10
crates9000 = ['']*10

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    if '[' in line:
        #proces input
        for j,s in enumerate(line):
            if s.isalpha():
                crates[1+int((j-1)/4)]=s+crates[1+int((j-1)/4)]
                crates9000[1+int((j-1)/4)]=s+crates9000[1+int((j-1)/4)]
    if 'move' in line:
        #proces movement
        p = re.compile(r'\d+')
        instr= [int(d) for d in p.findall(line)]
        #moves to
        crates[instr[2]]+=crates[instr[1]][-1-instr[0]+1:][::-1] #Movent n blocks from a to b, [::-1] reverses blocks
        crates9000[instr[2]]+=crates9000[instr[1]][-1-instr[0]+1:] #no reverse on crane9000
        
        #remove crates
        crates[instr[1]]=crates[instr[1]][:-instr[0]]
        crates9000[instr[1]]=crates9000[instr[1]][:-instr[0]]

message1 ='' 
message2 ='' 
for elementa,elementb in zip(crates,crates9000):
    if len(elementa)>0:
        message1 += elementa[-1]
    if len(elementb)>0:
        message2 += elementb[-1]

print("Part 1",message1)
print("Part 2",message2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))