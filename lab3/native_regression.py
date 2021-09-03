from matrix import *
import sys
import matplotlib.pyplot as plt

data = loadtxt(sys.argv[1])
X,Y = transpose(data)

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
Y2 = list(map(lambda x: b+m*x, X))

plt.plot(X,Y,"ro")
plt.plot(X,Y2)
plt.show()