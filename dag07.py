# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

folder_size = dict()
fol_cur='top'

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')

    if '$' in line:
        #Keep track of current folder, make dictionary of folders for the filesizes
        if '$ cd' in line:
            if '/' in line:
                fol_cur='top'
            elif '..' in line:
                fol_cur=fol_cur[:fol_cur.rfind('_')]
            else:
                fol_cur=fol_cur+'_'+line[5:]
            if fol_cur not in folder_size:
                folder_size.update({fol_cur:0})
            
    elif 'dir' in line:
        #Niet nodig, snel door
        continue
    else:
        f_size = int(re.match(r'\d+',line).group())
        
        #filesize is in all top folders: 
        folders=[fol_cur]
        
        #add list of top folders
        for i in range(0,len(fol_cur)):
            if fol_cur[i]=='_':
                folders.append(fol_cur[:i])
        
        #add filesize to all the folders
        for folder in folders:
            folder_size[folder]=folder_size[folder]+f_size
   
f.close()

del_size=0
for size in folder_size.values():
    if size<=100000:
        del_size+=size

disk_space = 70000000
upd_space  = 30000000
free_space = disk_space-folder_size['top']

space_needed = upd_space - free_space

smallest = 1000000000
for size in folder_size.values():
    if size>=space_needed:
        smallest=min(size,smallest)



print("Part 1",del_size)
print("Part 2",smallest)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))