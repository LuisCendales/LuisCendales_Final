import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("lista.dat")


plt.figure()
plt.plot(data[1,:], data[2;:])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Recorrido de partícula")
plt.savefig("CendalesLuis_final_15.pdf")
