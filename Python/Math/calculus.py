# from re import X
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

'''---------------------------------------------------------------------------------------------------- 119'''

x = sym.symbols('x')

fx = sym.sqrt(x+1) * sym.exp(-x)
gx = sym.cos(x + sym.sin(x))

fxx = sym.lambdify(x,fx)
gxx = sym.lambdify(x,gx)

xx = np.linspace(0,10,100)

plt.plot(xx,fxx(xx), label = "f(x)")
plt.plot(xx,gxx(xx), label = "g(x)")
plt.show()

lim_pnt = 5
lim_fx = sym.limit(fx,x,lim_pnt)
lim_gx = sym.limit(gx,x,lim_pnt)


lim_fgx = sym.limit(fx/gx,x,lim_pnt)

display(Math('\\frac{\\lim_{x\\to %g }f(x)} {\\lim_{x\\to %g }f(x)} = \
    \\frac{%g}{%g} = %g' \
    % (lim_pnt,lim_pnt, lim_fx, lim_gx, lim_fx/lim_gx)))



'''-----------------------------------------------------------------------------------------------------------------------------------120'''
from sympy.abc import X

piece1 = 0
piece2 = -2*x
piece3 = x**3/10

fx = sym.Piecewise((piece1, x<0),(piece2,(x>=0) & (x<10)),(piece3, x>=3))

fxx = sym.lambdify(x,fx)
xx = np.linspace(-3,15,1234)
plt.plot(xx,fxx(xx))

plt.show()

'''--------------''' # Exercise
piece1 = x**3
piece2 = sym.log(x,2) # Configuramos la base en el segundo argumento

fx = sym.Piecewise((piece1,x<=0),(piece2,x>0))

fxx= sym.lambdify(x,fx)
xx = np.linspace(-1,5,100)


with plt.xkcd(): # Este codigo es para darle a la grafico un estilo cmomo de nino
    plt.plot(xx,fxx(xx))
plt.show()


display(Math("f(x) = " + sym.latex(fx)))

'''-------------------------------------------------------------------------- 121 '''
# Derivatives

x = sym.symbols("x")

fx = x**2

dfx = sym.diff(fx)

# Aqui vienen tres de las mas famosas notaciones para el calclo diferencial

#Leibniz notacion 
display(Math("f(x) = %s, \\quad \\frac {df}{dx} = %s" % (sym.latex(fx), sym.latex(dfx))))




x = sym.symbols("x")

fx = x**2

dfx = sym.diff(fx)

# Aqui vienen tres de las mas famosas notaciones para el calclo diferencial

#Leibniz notacion -- german
display(Math("f(x) = %s, \\quad \\frac {df}{dx} = %s" % (sym.latex(fx), sym.latex(dfx))))


# Lagrange Notation -- french
display(Math("f(x) = %s, \\quad f'= %s" % (sym.latex(fx), sym.latex(dfx))))


# Newton Notation -- English
display(Math("f(x) = %s, \\quad \\dot{f}= %s" % (sym.latex(fx), sym.latex(dfx))))



import sympy.plotting.plot as symplot

fx = 3 - x**3

p = symplot(fx,(x,-5,5), show=False)
p.extend(symplot(sym.diff(fx),(x,-5,5), show=False))
p[1].line_color = "r"
p[0].line_color = "g"
p[0].lable = "$f(x) = %s$" % sym.latex(fx)
p[1].lable = "$f(x) = %s$" %sym.latex(sym.diff(fx))

p.legend = True

p.ylim = [-10,10]
p.show()



































































