# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def sort_custom(p2_list):

    for a in range(0,len(p2_list)):
        i=0
        while i<len(p2_list)-1-a:
            if compare(p2_list[i+1],p2_list[i],0)[0]==1: #Kijk of huidige waarde voor de volgende waarde moet blijven, zo nee:
                #swap twee waardes
                tmp = p2_list[i+1]
                p2_list[i+1] = p2_list[i]
                p2_list[i] = tmp        
            i+=1
            
    return p2_list

def parse(string):
    #Kijk of het een haakje is
    value=[]
    if len(string)==0:
        return value
    if string[0]!='[':
        #Het huidige element is een getal en geen lijst
        value.append(int(string.split(',')[0]))
        #Volgende komma is dan ook het begin van nieuw element
        loc=string.find(',')
        if loc>0:
            value.extend(parse(string[loc+1:]))
        return value
    
    if string[0]=='[':
        brack_count=1
        list_end=0
        while brack_count!=0:
            list_end+=1
            if string[list_end]==']':
                brack_count-=1
            if string[list_end]=='[':
                brack_count+=1

        value.append(parse(string[1:list_end]))
        if list_end<len(string)-1:
            value.extend(parse(string[list_end+2:]))
    return value

def compare(list1,list2,depth):
    right_order=1
    stop=0
        
    for element1,element2 in zip(list1,list2):
        #Als allebei een lijst zijn kunnen we een niveau dieper zoeken
        if type(element1) == type([]) and type(element2) == type([]):
            [right_order,stop]=compare(element1,element2,depth+1)
            
        #Als de een een getal is en de ander een lijst            
        elif type(element1) == type(1) and type(element2) == type([]):
            if len(element2)==0: #maar wacht de elementen zijn op in 2
                return [0,1]
            [right_order,stop]=compare([element1],element2,depth+1)
        
        #Als de een een getal is en de ander een lijst
        elif type(element1) == type([]) and type(element2) == type(1):
            if len(element1)==0: #maar wacht de elementen zijn op in 1
                return [1,1]
            [right_order,stop]=compare(element1,[element2],depth+1)
            
        #Finally test the digits, if right side is smaller it is not the right order
        elif element2<element1: return [0,1]
        elif element1<element2: return [1,1]
            
        #stop at any time it is not in the right order
        if stop==1: return [right_order,1]
    
    #Als we hier zijn gekomen was alles nog gelijk, vergelijk de lijstlengtes
    if len(list1)>len(list2):
        return [0,1]
    if len(list2)>len(list1):
        return [1,1]    
    #Geen probleem gevonden [1  maar nog niet stoppen! ,0]
    return [1,0]
        

f = open("input.txt", "r")
data=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(line)
    
f.close()

i=0
list1=list()
list2=list()
while i<len(data):

    list1.append(parse(data[i]))  
    list2.append(parse(data[i+1]))
    i+=3

total_1=0
count=0
for lijst1,lijst2 in zip(list1,list2):
    count+=1
    if compare(lijst1,lijst2,0)[0]==1:
        total_1+=count

div1=[[2]]
div2=[[6]]
p2_list=list1+list2+[div1]+[div2]
p3=sort_custom(p2_list)

loc1=p3.index(div1)+1
loc2=p3.index(div2)+1
print("Part 1",total_1)
print("Part 2",loc1*loc2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))