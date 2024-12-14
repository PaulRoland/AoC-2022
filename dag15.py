# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

f = open("input.txt", "r")
search_y=2000000
#search_y=10

#search_y=10
sensors=list()
beacons=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('\n','')
    [sens_x,sens_y,beac_x,beac_y]=[int(d) for d in re.findall(r'-?\d+',line)]
    sensors.append([sens_x,sens_y])
    beacons.append([beac_x,beac_y])
    #print(line)
f.close()


width_ranges=list()
for sensor,beacon in zip(sensors,beacons):
    distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    width = distance - abs(sensor[1]-search_y)
    if width>0:
        width_range=[sensor[0]-width,sensor[0]+width] #Van hier tot en met hier kan geen beacon
        width_ranges.append(width_range)
        
#combine ranges
width_ranges.sort()
total_range=list(width_ranges[0])
for width in width_ranges[1:]:
    if width[0]<=total_range[-1]: #Huidige range sluit aan bij vorige range
        if width[1]>total_range[-1]: #Total range mag wel wat groter worden
            total_range[-1]=width[1]
    else: #Huidige range sluit niet aan bij vorige range
        total_range.append(width[0])
        total_range.append(width[1])


online =list()
for beacon in beacons:
    if beacon[1] == search_y:
        online.append(beacon[0])

range_length=0
for a,b in zip(total_range[1::2],total_range[::2]):
    range_length+=(a-b)

print("Part 1",range_length-len(set(online))+len(total_range)//2) #Compenseer voor center ponits in total range

options=dict()
for sensor,beacon in zip(sensors[:],beacons[:]):
    distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1]) + 1 # Op afstand +1 zitten alle opties
    for a in range(0,distance+1):
        x1=sensor[0]+a
        y1=sensor[1]+distance-a
        x2=sensor[0]-a
        y2=sensor[1]-distance+a
        
        key1=str(x1)+'_'+str(y1)
        key2=str(x1)+'_'+str(y2)
        key3=str(x2)+'_'+str(y1)
        key4=str(x2)+'_'+str(y2)
        
        if x1>=0 and x1<=4000000:
            if y1>=0 and y1<=4000000:
                if key1 in options:
                    options[key1]+=1
                else:
                    options.update({key1:1})
                    
            if y2>=0 and y2<=4000000:
                if key2 in options:
                    options[key2]+=1
                else:
                    options.update({key2:1})
                    
        if x2>=0 and x2<=4000000:
            if y1>=0 and y1<=4000000:
                if key3 in options:
                    options[key3]+=1
                else:
                    options.update({key3:1})
                    
            if y2>=0 and y2<=4000000:
                if key4 in options:
                    options[key4]+=1
                else:
                    options.update({key4:1})

options_real=dict()
for key in options:
    if options[key]>=3:
        options_real.update({key:options[key]})
       
        
for option in options_real:
    possible=True
    
    width_ranges=list()
    search_y=int(option.split('_')[1])
    search_x=int(option.split('_')[0])
    for sensor,beacon in zip(sensors,beacons):
        distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        width = distance - abs(sensor[1]-search_y)
        if width>0:
            width_range=[sensor[0]-width,sensor[0]+width] #Van hier tot en met hier kan geen beacon
            width_ranges.append(width_range)
            
    #combine ranges
    width_ranges.sort()
    total_range=list(width_ranges[0])
    for width in width_ranges[1:]:
        if width[0]<=total_range[-1]: #Huidige range sluit aan bij vorige range
            if width[1]>total_range[-1]: #Total range mag wel wat groter worden
                total_range[-1]=width[1]
        else: #Huidige range sluit niet aan bij vorige range
            total_range.append(width[0])
            total_range.append(width[1])
            
    for a,b in zip(total_range[1::2],total_range[::2]):
        if search_x>=b and search_x<=a: #Hij valt binnen de range dat is niet goed
            possible=False
    
    if possible==True:
        #print(option,"moet het zijn")
        print("Part 2",search_x*4000000+search_y)
        break
        
               
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))