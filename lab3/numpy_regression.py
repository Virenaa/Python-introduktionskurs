from numpy import *
import sys

import matplotlib.pyplot as plt

def powers(powerlist, num1, num2):
    powerlisted = []
    for powers in powerlist:
        newRow =[]
        for i in range(num1, num2+1):
            newRow.append(powers**i)
        powerlisted.append(newRow)
    return array(powerlisted)

def poly(a,x):
    res = 0
    for n,coeff in enumerate(a):
        res += coeff*x**n

    return res

data = loadtxt(sys.argv[1])
n = int(sys.argv[2])

X,Y = transpose(data)
Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X2 = linspace(X[0], X[-1], int((X[-1]-X[0])/0.2)).tolist()
Y2 = list(map(lambda x: poly(a,x), X2))

plt.plot(X,Y,"ro")
plt.plot(X2,Y2)

plt.show()