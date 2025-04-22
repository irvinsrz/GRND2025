#1 Variable Scoping
#GLOBAL VARIABLES
y = "World"

#GLOBAL KEYWORD
def say():
    global y
    y = "Hello" #LOCAL VARIABLE
    


#LOCAL VARIABLES
def sayHello():
    x = "Hello" #Local Variable it can only acces inside this 
    print(x)
    print(y)


#PARAMETER VARIABLES
#def say(word):
    #print(word)

say()
print(y)                        

#2 Importing

#Import Arithmetic

#print(Arithmetic.add(5,10))

def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

#3 As Keyword
import constant as s
import arithmetic as a
import objects as o

c.pi
a.add(5,10)
o.student

#4 From Keyword

from arithmetic import add as a
from objects import student as s
from constant import pi as p

a(5,2)

s1 = student("Irvin","BSIT")

print(p)

#5 import another files to another files
import asd.arithmetic 
#or
import asd.arithmetic import add 


asd.arithmetic.add(5,10)

add(5,10)