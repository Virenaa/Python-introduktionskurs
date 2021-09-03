# tenta-210315

# 1

def username(program,first,last):
    return program.lower()[:3] + first.lower()[:2] + last.lower()[:2]

def create_username():
    program = input("Vilket program studerar du? ")
    name = input("Vad heter du? ").split()
    print("Ditt användarnamn är", username(program,name[0],name[1]))


# 2

from random import choice

def test_choice(values,repetitions):
   ress = {}
   for i in range(repetitions):
     c = choice(values)
     ress[c] = ress.get(c,0) + 1
   return ress


# 3

from graphics import *

class Target:
    def __init__(self,color1,color2,size):
        centre = Point(200,200)
        self.circles = []
        for i in range(size):
            circ = Circle(centre,200 - i*200/size)
            if i%2:
                color = color2
            else:
                color = color1
            circ.setFill(color)
            self.circles.append(circ)
            
    def draw(self,win):
        for circ in self.circles:
            circ.draw(win)
            
    def undraw(self):
        for circ in self.circles:
            circ.undraw()

