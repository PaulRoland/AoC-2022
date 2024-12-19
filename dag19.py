# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()


def iter_time(robots,minerals,could_buy,bought,time,costs,max_bots,max_rounds):
    global max_geode
    
    #Iets kopen in de echte laatste stap heeft toch geen zin.
    if time==max_rounds-1:
        geodes=minerals[3]+robots[3]
        if geodes>max_geode:
            max_geode=geodes
        return max_geode
    
    ##Maximaal bereikbare aantal geodes vanaf hier. 
    delta_t=max_rounds-time
    max_reachable=minerals[3]+delta_t*robots[3]+(delta_t)*(delta_t-1)/2
    if max_reachable<max_geode:
        #Mooie reden om wat eerder te stoppen
        return max_geode
    
    can_buy=[0,0,0,0]
    for j,cost in enumerate(costs):
        if minerals[0]>=cost[0] and minerals[1]>=cost[1] and minerals[2]>=cost[2]:
            if robots[j]<max_bots[j]:
                can_buy[j]=1

    minerals[0]+=robots[0]
    minerals[1]+=robots[1]
    minerals[2]+=robots[2]
    minerals[3]+=robots[3]
    
    for j,nbot in enumerate(robots):
        if can_buy[j]==1:
            
            #Een reden om iets niet nu nog te doen:
            if could_buy[j]==1 and bought==[0,0,0,0]: #Als ik hem in de vorige ronde had kunnen kopen, maar toen niets heb gekocht
                #Dan had ik hem beter eerder kunnen kopen en is dit geen ideale oplossing
                continue
            
            newbots=list(robots)
            newmins=list(minerals)
            
            newbought=[0,0,0,0]
            newbought[j]=1        
            
            newmins[0]-=costs[j][0]
            newmins[1]-=costs[j][1]
            newmins[2]-=costs[j][2]
            newmins[3]-=costs[j][3]
            newbots[j]+=1
            iter_time(newbots,newmins,can_buy,newbought,time+1,costs,max_bots,max_rounds)
    
    iter_time(list(robots),list(minerals),list(can_buy),[0,0,0,0],time+1,costs,max_bots,max_rounds)
    return max_geode
     

f = open("input.txt", "r")
prints=list()

for i,line in enumerate(f):
    info=[int(d) for d in re.findall(r'\d+',line)[1:]]
    
    #[ore,clay,obsidian,geode] cost per robot
    costs=[[info[0],0,0,0],[info[1],0,0,0],[info[2],info[3],0,0],[info[4],0,info[5],0]]
    prints.append(costs)    
f.close()


total_p1=0
for j,bp in enumerate(prints):
    #print(bp)
    max_robots=[0,0,0,0]
    max_geode=0
    
    #De hoogste prijs van elke grondstof bepaalt een bovengrens voor het aantal tekopen robots.
    #Het heeft geen zin om meer grondstoffen te maken dan je uit kan geven
    for cost in bp:
        max_robots[0]=max(max_robots[0],cost[0])
        max_robots[1]=max(max_robots[1],cost[1])
        max_robots[2]=max(max_robots[2],cost[2])
        max_robots[3]=99
        
    total_p1+=(j+1)*iter_time([1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0,bp,max_robots,24)

total_p2=1
for j,bp in enumerate(prints[:3]):
    #print(str(j+1)+':',bp)
    max_robots=[0,0,0,0]
    max_geode=0
    for cost in bp:
        max_robots[0]=max(max_robots[0],cost[0])
        max_robots[1]=max(max_robots[1],cost[1])
        max_robots[2]=max(max_robots[2],cost[2])
        max_robots[3]=99
        
    total_p2*=iter_time([1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0,bp,max_robots,32)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))