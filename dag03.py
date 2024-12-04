# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


total_prio = 0
badge_prio = 0

def find_prio(letter):
    if letter==letter.upper():
        return ord(letter) - 38
    if letter==letter.lower():
        return ord(letter) - 96
    return 0


f = open("input.txt", "r")

grouprs=['','','']

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    
    comp1=line[:int(len(line)/2)]
    comp2=line[int(len(line)/2):]
    match1=str(set(comp1).intersection(set(comp2)))[2]
    total_prio += find_prio(match1)
    
    #Keep track of last three lines
    grouprs[i%3]=line
    #Every third line find match between the three lines
    if i%3 == 2:
        match2 = str(set(grouprs[0]).intersection(set(grouprs[1])).intersection(set(grouprs[2])))[2]
        badge_prio+=find_prio(match2)
    
f.close()

print("Part 1:",total_prio)
print("Part 2:",badge_prio)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))