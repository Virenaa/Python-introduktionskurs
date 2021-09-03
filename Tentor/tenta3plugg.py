
# Fråga 1
def pandemic_rules(ownpro,pop,cases):
    pro = cases * 100000 / pop
    if pro <ownpro and pro < 25:
        return("grönt")
    elif pro < 50 and pro >= 25:
        return("gult")
    else:
        return("rött")

def apply_pandemic_rules(ownpro):
    pop = int(input("Hur stor är ditt lands befolkning?"))
    cases = int(input("Hur många fall har ditt land haft?"))
    color =pandemic_rules(ownpro,pop,cases)
    print("Ditt land är" + color + ".")


# Fråga 2
def div9(n):
    ds = list(str(n))
    while len(ds)>1:
        r = 0
        for d in ds: 
            r = r + int(d)
        print(r)
        ds = list(str(r))
    r = int(ds[0])
    return r == 9
    
from graphics import *

# Fråga 3
class Chessboard: 

    def __init__(self, black, white,size):
        self.black = black
        self.white = white
        self.sqsize = size
    
    def draw(self):
        win = GraphWin("Schackbräddet" , 8*self.sqsize, 8*self.sqsize, autoflush=False)
        for x in range(8):
            for y in range(8):
                square = Rectangle(Point(self.sqsize*x,self.sqsize*y),Point(x*self.sqsize+self.sqsize,y*self.sqsize+self.sqsize))
                if ((x%2 == 0 and y%2 == 0) or (x%2 > 0 and y%2 > 0)):
                    square.setFill(self.white)
                else:
                    square.setFill(self.black)
                square.draw(win)



