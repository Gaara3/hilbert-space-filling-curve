#!/bin/python
from sys import argv
import  turtle
turtle.speed(0)
iter = argv[1]
print iter, "iter"
striter = str(iter)
#print striter[::-1]
def reverse(x):
    return x[::-1]
def flip(x):
    product = ""
    for i in x:
        
        if i == "1":
            product = product + "0"
        elif i == "0":
            product = product + "1"
        else:
            product = product + "3"
    return product


#print inverse("110")

#x = reverse(striter)
#print inverse(x)

#######
"""
jusq'ici j'ai la fonction reverse et inverse

"""
#######
base = "00"
rol = base
for i in range(int(iter)):
    if (i + 1) % 2 != 0:
        a = "03"
        b = "11"
        rol = flip(rol) + a + rol + b + rol + reverse(a) + flip(rol)
    else:
        a = "30"
        b = "33"
        rol = flip(rol) + a + rol + b + rol + reverse(a) + flip(rol)
new = rol
#print nextiter(striter)

#print nextiter("1110110110010011101100100100")
printans=raw_input('Display r/l form?(y/n):')
#if yes, print the iteration
if printans=='y':
    print(new)
r = '0'
l = '1'
f = "3"
#prepare to display the graphics
#do not show the turtle icon when drawing











pencolor = "black"
bgcolor = "white"
length = int(argv[2])
turtle.ht()
#set drawing speed to fastest(no animation)

#set pen color as requested
turtle.color(pencolor)
#set background color as requested
turtle.bgcolor(bgcolor)

#display segment of desired length to build off of
turtle.forward(length)

#cycling through all the characters in the iteration
for char in range(0,len(new)):
    #if the character is a right:
    if new[char] == (r):
        #turn right at a right angle 
        turtle.right(90)
        #go forward desired length
        turtle.forward(length)
    #otherwise, if the character is a left:
    elif new[char] == (l):
        #turn left at a right angle
        turtle.left(90)
        #go forward desired length
        turtle.forward(length)
    elif new[char] == (f):
        turtle.forward(length)
print len(new)
i = raw_input("quit ?")
