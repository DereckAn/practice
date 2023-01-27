from re import X
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math


'''---------------------------------------------------------------------------------------------------------------------118'''
# Computing limist of a function. 

x = sym.symbols('x')

fx = x**3
lim_point = 1.5 
lim = sym.limit(fx, x, lim_point)

print(lim)
display(Math("\\lim_{x\\to %g} %s = %s" % (lim_point, sym.latex(fx), lim)))

fxx = sym.lambdify(x,fx) 
xx = np.linspace(-5,5,200)

plt.plot(xx,fxx(xx))
plt.plot(lim_point, lim, 'ro')
plt.plot([1.5,1.5],[-100,100],"--")
plt.plot([2,2],[-100,100],"--")

plt.grid()
plt.show()



fx = (x**2)/(x-2)
fxx = sym.lambdify(x,fx)
xx = np.linspace(1,3,102)

lim_pnt = 2
lim = sym.limit(fx,x,lim_pnt, dir = '-')

plt.plot(xx,fxx(xx))
display(Math("\\lim_{x\\to %g^-} %s = %s" % (lim_point, sym.latex(fx), lim)))

plt.show()
























































































