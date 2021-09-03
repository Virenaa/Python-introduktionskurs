# file python_exam.py

# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

from graphics import *

# 1

def pandemic_rules(ownproportion,population,cases):
    proportion = cases * 100000 / population
    if proportion < ownproportion:
        return('grönt')
    elif proportion < 25:
        return('grönt')
    elif proportion < 50:
        return('gult')
    else:
        return('rött')

def apply_pandemic_rules(ownproportion):
    population = int(input("Hur stor är ditt lands befolkning? "))
    cases = float(input("Hur många fall ditt land haft? "))
    colour = pandemic_rules(ownproportion,population,cases)
    print("Ditt land är " + colour + ".")

# 2

def div9(n):
    ds = list(str(n))
    while len(ds) > 1:
        r = 0
        for d in ds:
            r = r + int(d)
        print(r)
        ds = list(str(r))
    r = int(ds[0])
    return r == 9

# 3

class Chessboard:
    def __init__(self,black,white,size):
        self.black = black
        self.white = white
        self.sqsize = size
    def draw(self):
        sq = self.sqsize
        win = GraphWin("Schackbrädet",8*sq,8*sq)
        for x in range(8):
            for y in range(8):
                square = Rectangle(Point(x*sq,y*sq),Point(x*sq+sq,y*sq+sq))
                if ((x%2 == 0 and y%2 == 0) or (x%2 > 0 and y%2 > 0)):
                    square.setFill(self.white)
                else:
                    square.setFill(self.black)
                square.draw(win)

