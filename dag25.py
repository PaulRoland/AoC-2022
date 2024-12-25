# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")

total=0
getallen = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('\n','')
    
    number=0
    for n,s in enumerate(line[::-1]):
        number+=getallen[s]*5**n
    total+=number
    print(line,number)
f.close()

part1=total
#Convert total to snafu
getal_rev = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
numbers=[0 for d in range(0,30)]

for n,_ in enumerate(numbers):
    power=len(numbers)-n-1
    b=round(total/5**power)
    b=min(b,2)
    total-= b*5**power
    numbers[n]=b
     
getal_rev = {2:'2',1:'1',0:'0',-1:'-',-2:'='}
SNAFU=''
started=False
for n in numbers:
    if n!=0:
        started=True
    if started==True:
        SNAFU+=getal_rev[n]
    
print("Part 1",part1,SNAFU)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))