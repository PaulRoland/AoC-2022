# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def monkey_value(key):
    if monkeys[key][2]=='=':
        monkeys[key][0]=monkeys[key][3]
        return monkeys[key][3]
    
    else:
        monkey1=monkey_value(monkeys[key][1])
        monkey2=monkey_value(monkeys[key][3])
        
    if monkeys[key][2]=='*': return monkey1*monkey2
    if monkeys[key][2]=='+': return monkey1+monkey2
    if monkeys[key][2]=='/': return monkey1/monkey2
    if monkeys[key][2]=='-': return monkey1-monkey2

def monkey_value2(key): #return number or the calculation string/expression
    if key=='humn':
        return 'X'
    
    if monkeys[key][2]=='=':
        return str(monkeys[key][3])
    else:
        monkey1=monkey_value2(monkeys[key][1])
        monkey2=monkey_value2(monkeys[key][3])
    
    #Stuur de twee vergelijkingen terug die gelijk moeten zijn
    if key=='root':
        return [monkey1,monkey2]
    
    #Return de berekening als string
    return '('+monkey1+monkeys[key][2]+monkey2+')'
        
f = open("input.txt", "r")
monkeys=dict()
for i,line in enumerate(f):
    match=re.findall(r'\w{4}',line)
    key=match[0]
    
    if len(match)>1:
        calc=re.findall(r'[\+\/\*\-]',line)
        monkeys.update({key:[0,match[1],calc[0],match[2]]})
    
    if len(match)==1:
        number=int(line.split(':')[1])
        monkeys.update({key:[0,key,'=',number]})
    
f.close()

[a,b]=monkey_value2('root')
import sympy as sp
X = sp.symbols('X')
#A can be a string or a number, variable in string is X
if type(a)==type('a'):
    sympy_eq_a=sp.parse_expr(a)
else:
    sympy_eq_a=a
    
if type(b)==type('b'):
    sympy_eq_b=sp.parse_expr(b)
else:
    sympy_eq_b=b
print(a,'\nequals\n',b)
soln=sp.solve(sp.Eq(sympy_eq_a,sympy_eq_b),X)
total_p2=int(soln[0].evalf())

print("Part 1",int(monkey_value('root')))
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))