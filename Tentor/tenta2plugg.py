# Fråga 1 
from Tentor.tenta2 import postorder
from sys import prefix


def movieTickets():
    count = int(input("Hur många biljetter vill du köpa?"))
    minor = int(input("Hur många av er är under 18 år?"))
    time = int(input("Vilken föreställning (ange klockslag i hela timmar)?"))
    price = (count - minor)*100 + minor*50  

    if time <18:
        price = price *9/10

    print("Biljetterna kostar sammanlagt ", price, "kr.")


#Fråga 2 

def pepLineLength(filename):
    file = open (filename)
    lines = file.readLines() 
    character_length = 0
    for character in len(lines):
        if len(lines[character]) > 79:
            print("line",character+1, "too long:",len(lines[character]))
            character_length += 1
    print(character_length, "are too long")


#Fråga 3
class Tree:
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees
    
    def getParts(self):
        return self.root, self.subtrees

    def preorder(tree):
        node, trees = tree.getParts()
        nodes = [node]
        for t in trees:
            nodes = nodes + preorder(t)
        return(nodes)

    def postorder(tree):
        node, trees = tree.getParts()
        nodes =[]
        for t in trees:
            nodes = nodes + postorder(t)
        nodes.append(node)
        return(nodes)
    
royals = Tree("CarlGustaf", 
        [Tree(("Victoria"),[Tree("Estelle",[]),Tree("Oscar")]),
        Tree("CarlPhilip",[Tree("Alexnader",[])]),
        Tree("Madeleine",[Tree("Leonore",[]),Tree("Nicolas",[])])])




def main():
    #movieTickets()
    pepLineLength()

main()

