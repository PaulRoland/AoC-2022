# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import re
import time
start_time = time.time_ns()
import math

data=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(line)
f.close()

mk_list=list()
for i in range(0,round(len(data)/7)):
    items = [int(d) for d in re.findall(r'\d+',data[i*7+1])]
    
    if 'old * old' not in data[i*7+2]:
        operator = data[i*7+2].split('old ')[1][0]
        factor = [int(d) for d in re.findall(r'\d+',data[i*7+2])][0]
    else:
        factor = 2
        operator = '^'
    divisor = [int(d) for d in re.findall(r'\d+',data[i*7+3])][0]
    monkey_t = [int(d) for d in re.findall(r'\d+',data[i*7+4])][0]
    monkey_f = [int(d) for d in re.findall(r'\d+',data[i*7+5])][0]
    
    mk_list.append([items,operator,factor,divisor,monkey_t,monkey_f,0])
    
for i in range(0,20):
    for monk in mk_list:
        for item in monk[0]:
            if monk[1] == '*': worry=item*monk[2]
            elif monk[1] == '/': worry=item/monk[2]
            elif monk[1] == '+': worry=item+monk[2]
            elif monk[1] == '-': worry=item-monk[2]
            elif monk[1] == '^': worry=item**monk[2]
            
            worry=int(worry/3)

            if worry%monk[3]==0:
                mk_list[monk[4]][0].append(worry)
            else:
                mk_list[monk[5]][0].append(worry)
            monk[6]+=1
        monk[0]=[]


monkey_scores = [monk[6] for monk in mk_list]
monkey_scores.sort()
print("Part 1",monkey_scores[-1]*monkey_scores[-2])

mk_list=list()
for i in range(0,round(len(data)/7)):
    items = [int(d) for d in re.findall(r'\d+',data[i*7+1])]
    
    if 'old * old' not in data[i*7+2]:
        operator = data[i*7+2].split('old ')[1][0]
        factor = [int(d) for d in re.findall(r'\d+',data[i*7+2])][0]
    else:
        factor = 2
        operator = '^'
    divisor = [int(d) for d in re.findall(r'\d+',data[i*7+3])][0]
    monkey_t = [int(d) for d in re.findall(r'\d+',data[i*7+4])][0]
    monkey_f = [int(d) for d in re.findall(r'\d+',data[i*7+5])][0]
    
    mk_list.append([items,operator,factor,divisor,monkey_t,monkey_f,0])


f = math.lcm(11,5,19,13,7,17,2,3)

for i in range(0,10000):
    for monk in mk_list:
        for item in monk[0]:
            if monk[1] == '*': worry=item*monk[2]
            elif monk[1] == '/': worry=item/monk[2]
            elif monk[1] == '+': worry=item+monk[2]
            elif monk[1] == '-': worry=item-monk[2]
            elif monk[1] == '^': worry=item**monk[2]
            
            #worry=int(worry/3)
            worry=worry%f
            if worry%monk[3]==0:
                mk_list[monk[4]][0].append(worry)
            else:
                mk_list[monk[5]][0].append(worry)
            monk[6]+=1
        monk[0]=[]

monkey_scores = [monk[6] for monk in mk_list]
monkey_scores.sort()
print("Part 2",monkey_scores[-1]*monkey_scores[-2])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))