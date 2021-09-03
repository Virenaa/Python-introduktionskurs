# exam 2020-08-28

# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentatiden 8:30-10:30.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

# 1

def movieTickets():
    number = int(input("Hur många biljetter vill du köpa? "))
    youngs = int(input("Hur många av er är under 18 år? "))
    time   = int(input("Vilken föreställning (ange klockslag i hela timmar)? "))

    price = (number-youngs)*100 + youngs*50
    if time < 18:
        price = price * 9 // 10
        
    print("Biljetterna kostar sammanlagt", price, "kr.")

# 2

def pepLineLength(filename):
    "warn about lines longer than 79 characters"
    file = open(filename)
    lines = file.readlines()
    linecount = 0
    longcount = 0
    for i in range(len(lines)):
        if len(lines[i]) > 79:
            print("line",i+1,"too long:", len(lines[i]))
            longcount += 1
    print(longcount,"lines were too long")

# 3

#given
class Tree:
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees

    def getParts(self):
        return self.root, self.subtrees

def preorder(tree):
    node,trees = tree.getParts()
    nodes = [node]
    for t in trees:
        nodes = nodes + preorder(t)
    return(nodes)

def postorder(tree):
    node,trees = tree.getParts()
    nodes = []
    for t in trees:
        nodes = nodes + postorder(t)
    nodes.append(node)
    return(nodes)

royal = Tree('CarlGustaf',
             [Tree('Victoria',[Tree('Estelle',[]),Tree('Oscar',[])]),
              Tree('CarlPhilip',[Tree('Alexander',[])]),
              Tree('Madeleine', [Tree('Leonore',[]), Tree('Nicolas',[])])])


