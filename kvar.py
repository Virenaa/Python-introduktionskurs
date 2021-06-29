sal= int(input("Ange bruttolön:"))
tax=int(input("Ange skatteprocent:"))
rent=int(input("Ange hyra:"))

tax=sal*tax/100
net=sal-tax
remains=net - rent 

print("Kvar:", remains)



