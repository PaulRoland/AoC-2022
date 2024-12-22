# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time

start_time = time.time_ns()

decryptionkey = 811589153
f = open("input.txt", "r")
numbers=list()
numbers2=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    #Maak een lijst van 
    #[getal,original_index]
    numbers.append([int(line),i])
    numbers2.append([int(line)*decryptionkey,i])
f.close()

i=0
while i<len(numbers):
    #Dit is niet best
    #Zoek volgende movenumbers uit oorspronkelijke volgorde
    for index,[movenumber,org_index] in enumerate(numbers):
        if org_index==i: 
            break
    
    #Verwijder huidige getal en bepaal de locatie
    del numbers[index]
    #de modulo is dus ook een getal lager, echt smerig.
    numbers.insert((index+movenumber)%len(numbers),[movenumber,org_index])
    i+=1
    

for j,[movenumber,org_index] in enumerate(numbers):
    if movenumber==0: #zoek volgende movenumbers
        ind=j
        break
print("Part 1",numbers[(ind+1000)%len(numbers)][0]+numbers[(ind+2000)%len(numbers)][0]+numbers[(ind+3000)%len(numbers)][0])


#print("Part 2")
#Zelf als hierboven, maar mix 10 times en de getallen zijn hoger *decryptionkey
for _ in range(0,10):
    i=0
    while i<len(numbers2):   

        for index,[movenumber,org_index] in enumerate(numbers2):
            if org_index==i: 
                break
            
        del numbers2[index]
        numbers2.insert((index+movenumber)%len(numbers2),[movenumber,org_index])
        i+=1
  
for j,[movenumber,org_index] in enumerate(numbers2):
    if movenumber==0: #zoek volgende movenumbers
        ind=j
        break
print("Part 2",numbers[(ind+1000)%len(numbers)][0]+numbers[(ind+2000)%len(numbers)][0]+numbers[(ind+3000)%len(numbers)][0])

print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))