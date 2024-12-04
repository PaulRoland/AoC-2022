# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import numpy as np
import time
start_time = time.time_ns()



f = open("input.txt", "r")
#f = open("input.txt", "r")
elf=0
calories=0
calories_highest=0
calories_list=list()

calories_list.append(0)
for i,line in enumerate(f):
    print(len(line))
    if len(line)>3:
        calories=calories+int(line)
        calories_list[elf]=calories
    else:
        #Nieuwe elf wordt beschreven vanaf nu
        elf+=1
        calories_list.append(0)
        calories=0
    
f.close()





calories_list.sort()



print("Part 1",calories_list[-1])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
print("Part 2",calories_list[-1]+calories_list[-2]+calories_list[-3])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))