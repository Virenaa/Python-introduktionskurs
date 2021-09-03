#Uppgift 1

def username(program, firstname, lastname):
    return program.lower()[:3] + firstname.lower()[:2] + lastname.lower()[:2]

def create_username(): 
    pogram = input("Vilket pogram studerar du?")
    namn = input("Vad heter du?").split()

    print("Ditt användarnamn är " + username(pogram,namn[0], namn[1]) )



#Fråga 2
from random import choice

def test_choice(values, repetitions):
    dict = {}
    # Skapar en dict med values = nycklar 
    # repetioner = värden
    for rep in range(repetitions):
        key = choice(values)
        dict[key] = dict.get(key,0) +1 #get(key,default)
    print(dict)
    return dict 


# Fråga 3
from graphics import *

class Target: 

    def __init__(self,col1, col2, count):
        self.win = GraphWin("Target", 400, 400)
        centre= Point(200,200)
        self.circles = []

        for i in range(count):
            circ = Circle(centre,200 - 200*i/count )
            if 1%2:
                color = col1 
            else:
                color=col2
            circ.setFill(color)
            self.circles.append(circ)

            
    def draw(self,win):
        for circ in self.circles:
            circ.draw(win)

    def undraw(self):
            for circ in self.circles:
                circ.undraw()


def main(): 
    #create_username()
    #test_choice(range(1,7),6000)
    print(range(7))
main()

