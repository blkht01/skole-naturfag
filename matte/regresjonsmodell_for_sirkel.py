import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def modell(x,a,b):
    return a*x + b

X = [0.31, 1.40,2.30,3.30]
Y = [1.95,8.80,14.45,20.73]

konstanter, kovarians = curve_fit(modell, X,Y)

a,b = konstanter

print(f'f(x)= {a:.2f}x+{b:.3f}')

#tegner modellen vi fant, sammen med punktene

X_2 = np.array(X)
Y_2 = modell(X_2,a,b)

plt.plot(X_2,Y_2)    #tegner modellen

plt.scatter(X,Y)     #tegner målepunktene

plt.show()