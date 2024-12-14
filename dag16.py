# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def shortest_dist(cur_node,end_node,cur_dist,visited):
    global shortest
    #Als we er zijn
    if cur_node == end_node:
        shortest=min(shortest,cur_dist)
        return
    #Als het pad te lang begint te worden
    if cur_dist >= shortest:
        return
    
    for [next_node,cost] in graph[cur_node][1]:
        if next_node not in visited:
            new_visited=list(visited)
            new_visited.append(next_node)
            shortest_dist(next_node,end_node,cur_dist+cost,new_visited)
    

def open_valve(total_pressure,time_left,current_valve,valves_opened,times):
    global max_pressure
    
    if time_left>0:       
        #Calculate if it is worth it to continue this path
        heuristic=0
        prio=list()
        for [key,dist] in distances[current_valve]:
            if key not in valves_opened:
                prio.append([graph[key][0]*(time_left-dist),key,dist])
                heuristic+=graph[key][0]
        
        #Groffe heuristic, maar helpt vast een beetje
        if total_pressure+time_left*heuristic < max_pressure:
            return
        
        prio.sort(reverse=True)
        for value,valve,time_cost in prio:
            new_valves=list(valves_opened)
            new_times=list(times)
            new_press=total_pressure
            
            new_valves.append(valve)
            new_time=time_left-time_cost             
            new_times.append(new_time)
            new_press+=value       
            if new_time>0:
                open_valve(new_press,new_time,valve,new_valves,new_times)
        
    #no time left check result   
    if total_pressure>max_pressure:
        #print("grotere optie gevonden",total_pressure)
        max_pressure=max(max_pressure,total_pressure)
        #print(valves_opened)
        #print(times)
    return 

def open_valve2(total_pressure,time_left_self,time_left_elep,cur_valve_self,cur_valve_elep,valves_opened,times):
    global max_pressure
    if time_left_self<0 and time_left_elep<0:
        return
        
    global counter
    heuristic1=0
    heuristic2=0
    prio_self=list()
    if time_left_self>0:
        for [key,dist] in distances[cur_valve_self]:
            
            if key not in valves_opened and graph[key][0]*(time_left_self-dist)>0:
                prio_self.append([graph[key][0]*(time_left_self-dist),key,dist])
                #Tel alle mogelijke opties op, als groffe heuristic
                heuristic1+=graph[key][0]*(time_left_self-dist)
    

    prio_elep=list()    
    if time_left_elep>0:       
        for [key,dist] in distances[cur_valve_elep]:
            if key not in valves_opened and graph[key][0]*(time_left_elep-dist)>0:
                prio_elep.append([graph[key][0]*(time_left_elep-dist),key,dist])
                #Tel alle mogelijke opties op, als groffe heuristic
                heuristic2+=graph[key][0]*(time_left_elep-dist)
    
    #Groffe heuristic gebruiken om te kijken of het zin heeft om door te gaan
    #Gaat goed tot factor 0.38, dus iets robuustere factor genomen
    #Zet op 1 als je sowieso geen risico wil
    if total_pressure+0.5*(heuristic1+heuristic2) < max_pressure:
        return
    
    prio_self.sort(reverse=True)
    prio_elep.sort(reverse=True)
    
    ##Als we allebei nog ergens heen kunnen
    if len(prio_self)>0 and len(prio_elep)>0:        
        for value1,valve1,time_cost1 in prio_self:
            for value2,valve2,time_cost2 in prio_elep:
                
                if valve1==valve2: #We kunnen niet naar dezelfde plek gaan
                    continue
                
                new_valves=list(valves_opened)
                new_times=list(times)
                new_press=total_pressure
                
                new_time_self=time_left_self
                new_time_elep=time_left_elep
                
                if time_left_self-time_cost1>=0:
                    new_time_self=time_left_self-time_cost1
                    new_times.append(new_time_self)    
                    new_valves.append(valve1)
                    new_press+=value1
                
                
                if time_left_elep-time_cost2>=0:
                    new_time_elep=time_left_elep-time_cost2
                    new_times.append(new_time_elep)    
                    new_valves.append(valve2)
                    new_press+=value2
                
                if new_press!=total_pressure: #Kijk even of er iets veranderd is, of niet aan de voorwaarden is voldaan
                    open_valve2(new_press,new_time_self,new_time_elep,valve1,valve2,new_valves,new_times)
                    
    elif len(prio_self)>0: #Olifant kan nergens meer heen en heeft geen tijd meer, maar ik kan door
        for value1,valve1,time_cost1 in prio_self:
            new_valves=list(valves_opened)
            new_times=list(times)
            new_press=total_pressure

            new_time_self=time_left_self-time_cost1
            new_times.append(new_time_self)  
            
            new_valves.append(valve1)
            new_press+=value1
            open_valve2(new_press,new_time_self,0,valve1,cur_valve_elep,new_valves,new_times)
            
    elif len(prio_elep)>0: #Ik kan nergens meer heen, maar de olifant kan door  
        for value2,valve2,time_cost2 in prio_elep:
            new_valves=list(valves_opened)
            new_times=list(times)
            new_press=total_pressure

            new_time_elep=time_left_elep-time_cost2
            new_times.append(new_time_elep)    
            
            new_valves.append(valve2)
            new_press+=value2
            open_valve2(new_press,0,new_time_elep,cur_valve_elep,valve2,new_valves,new_times)        
        
    #no time left check result   
    if total_pressure>max_pressure:
        #print("grotere optie gevonden",total_pressure)
        max_pressure=max(max_pressure,total_pressure)
        #print(valves_opened)
        #print(times)
    return 

        
f = open("input.txt", "r")
graph=dict()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('\n','')
    keys=re.findall(r'[A-Z]{2}',line)
    flow_rate=int(line.split('=')[1].split(';')[0])
    graph.update({keys[0]:[flow_rate,[[keys[1],1]]]})
    
    for key in keys[2:]:
        graph[keys[0]][1].append([key,1])
f.close()


## try to reduce the graph
keys_to_remove=list()
for key in graph:
    #print(key)
    if graph[key][0]==0 and key!='AA': #Als er geen flow is dan kijken of we hem uit de som kunnen halen
        if len(graph[key][1])==2: #directe tunnel, geen splitsingen
        
            l2=graph[key][1][0][1]
            l3=graph[key][1][1][1]
            new_l=l2+l3
            
            key2=graph[key][1][0][0]
            key3=graph[key][1][1][0]
            #print(graph[key2][1])
            #print(graph[key3][1])
            
            graph[key2][1].append([key3,new_l])
            graph[key2][1].remove([key,l2])
            
            graph[key3][1].append([key2,new_l])
            graph[key3][1].remove([key,l3])
            
            keys_to_remove.append(key)
            #print(graph[key2][1])
            #print(graph[key3][1])
for key in keys_to_remove:
    del graph[key]

distances=dict()
all_keys=list(graph.keys())
for start in all_keys:
    dist=list()
    dist.append([start,1]) #Open zelf duurt 1 minuut
    for end in all_keys:
        if start!=end:
            shortest=99999
            shortest_dist(start,end,0,[])    
            dist.append([end,shortest+1]) #Reistijd + one more minute to open
    distances.update({start:dist})
    
max_pressure=2000
open_valve(0,30,'AA',[],[])
total_p1=max_pressure

max_pressure=0
open_valve2(0,26,26,'AA','AA',[],[])
total_p2=max_pressure

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))