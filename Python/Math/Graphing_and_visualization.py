from cProfile import label
import sympy as sym
import matplotlib.pyplot as plt 
from sympy.abc import w,x,y,z
import math
import numpy as np



# El orden de los metodos importa mucho. 

x = 3
y = 5

plt.plot(x,y,'ro') # Esto es para graficar los puntos.    ro  --> red circle. 
plt.plot(x-1,y-1,"gs") # gs   ---> green square  
plt.plot(x-2,y-2,"kp") # kp ---> Black pentagon
plt.axis("square") # Esto es para hacer la grafica cuadrada
plt.axis([-6,6,-5,5]) # Esto es para delimitar los limites de la grafica. Los dos primeros numerso seran para el eje de la x y los dos ultimos seera para el eje y 
plt.grid() # Este metodo es para cuadricular fla grafica. 
plt.show() # Este es para mostrar en pantalla. --> similar al metodo print()

'''----------------------------------------------------------------------------------------------------------------'''

x = [-4,5,2,4,5,6,3]
y = [0,3,4,5,2,-3,4]

for i in range(0,len(x)):
    plt.plot(x[i], y[i], "o", label ="point %s" % (1+i)) # Esto es plo que tendra la etiqueta.

plt.axis("square")
plt.grid()
plt.legend() # Este metodo es para activar las etiquetas. 
plt.show()



'''----------------------------------------------------------------------------------------------------------------- 53'''


plt.plot(4,2,"r+")

axis = plt.gca() # Este metodo significa "Get Curent Axis"
ylim = axis.get_ylim()
print(ylim) #(1.89, 2.1100000000000003)  Esto son los limites del eje "y"

axis.set_ylim([ylim[0], 5.3987654]) 
ylim = axis.get_ylim()
print(ylim) # (1.89, 5.3987654) 

plt.show()


'''------------------------------------------------------------------------------------------------------------------ 54 '''
# Exercise 

x = sym.symbols("x")
y = x**2 - 3*x

for i in range(-10,11):
    plt.plot(i,y.subs(x,i), "o")
    
plt.xlabel("x")
plt.ylabel("f(x) = %s" % y)

plt.show()



# Este ejercicio es por mi cuenta. Vamos a graficar una ecuacion cubica.  con rango x{-15:16}
# x = sym.symbols("x")  # invetigar por que esta cosa no funciona is este metodo. 
y = 3*x**3 + 2*x**2 - 9*x + 10

for i in range(-15,16):
    plt.plot(i, y.subs(x,i), "o")

plt.grid()
plt.show()



'''------------------------------------------------------------------------------------------------------------------------ 55 '''
# Graphing lines     

# Lines un start/stop form.

p1 = [-3, -1]
p2 = [4,4]

plt.plot(p1, p2)  # Si lo ponemos asi solo nos aparece una grafica con una linea recta en el centro horiontalmente. 

plt.plot([p1[0],p2[0]], [p1[1], p2[1]], color=[.5,.3,.8], linewidth = 5)  # la primer lista es para el inicio de la linea  y la ultima lista es para el final de la linea. 
# La ultima lista es para escoger el color  --> tipo RGB      >> COLOR
# Es para cambiar el grosor de la linea.                      >> LINEWIDTH  
plt.axis("square")
plt.axis([-6,6,-6,6])
plt.show()

#----------------------------------------------

x = 3
y = 5

plt.plot(x,y,"ro")
plt.plot([0,x], [0,y], 'r')

plt.axis("square")
plt.axis([-6,6,-6,6])
plt.grid()
 
plt.plot([-6,6], [0,0], 'k', linewidth = 3)
plt.plot([0,0], [-6,6], 'k', linewidth = 3)
plt.show()


# ---------- Exercise
# mio -- para mas referencias busca en el ipad. En la libreta de "Data Science"
plt.plot([0,0], [0,2], 'g')
plt.plot([0,2], [0,0] , 'k')
plt.plot([2,0], [2,2], 'r')
plt.plot([2,2], [0,2], 'b')

plt.axis("square")
plt.axis([-3,5,-3,5])
plt.title("A colorful square")
plt.show()



y = abs(x)**(1/2)
# y = np.sqrt(abs(x))

for i in range(-20,21):
    # plt.plot([0,i],[0,y.subs(x,i)])    ----> Me daba error cuando trataba de usar el metodo ".subs()"
    plt.plot([0,i], [0, abs(i)**(1/2)])

plt.show()

'''---------------------------------------------------------------------------------------------------------------------- 56'''
# Lines in slope intercept form.    Y = mx + b

x = [-5,5]
m = 2
b = 1

y = [340, 2345]
for i in range(0,len(x)):
    y[i] = m*x[i] + b
    
print(x,y)   # [-5, 5] [-9, 11]
plt.plot(x,y, label = "y = %sx + %s" % (m,b) )
plt.axis("square")
plt.xlim(x)
plt.ylim(x)
plt.legend() # Activar las etiquetas
plt.grid()

axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0], "k--")
plt.plot([0,0], axis.get_ylim(), "k--")

plt.show()


# --------------------------------------------------- Solucion numpy

x = [-5,5]
m = 3
b = 2

y = m*np.array(x) + b  #  <<--  solucion numpy

plt.plot(x,y, label = "y = %sx + %s" % (m,b) )
plt.axis("square")
plt.xlim(x)
plt.ylim(x)
plt.legend() # Activar las etiquetas
plt.grid()

axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0], "k--")
plt.plot([0,0], axis.get_ylim(), "k--")

plt.show()

# --------------------------------------------------Exercise

x = [-5,5]
b1 = -2
m1 = .7

y = [-234,234]
for i in range(0,len(x)):
    y[i] = m1*x[i] + b1
plt.plot(x,y, label = "y = %sx + %s" % (m1,b1))

m2 = -1.25
b2 = .75

y = m2*np.array(x) + b2
plt.plot(x,y, label = "y = %sx + %s" % (m2,b2))


plt.axis("square")
plt.xlim(x)
plt.ylim(x)
plt.legend()
plt.grid()

axis = plt.gca()
plt.plot(axis.get_xlim(), [0,0], "k--")
plt.plot([0,0], axis.get_ylim(), "k--")

plt.show()
    

# ------------------------------------------  resultado de profesor 
x = [-5,5]
m = [.7, -1.75]
b = [-2, .75]

for i in range(0, len(m)):
    y = m[i]*np.array(x) + b[i]
    plt.plot(x,y, label = "y = %sx + %s" % (m[i],b[i]))

plt.axis("square")
plt.xlim(x)
plt.ylim(x)
plt.legend()
plt.grid()

axis = plt.gca()
plt.plot(axis.get_xlim(), [0,0], "k--")
plt.plot([0,0], axis.get_ylim(), "k--")

plt.show()



'''---------------------------------------------------------------------------------------------------------------------- 57'''
#  Graphing rational functions.      

x = range(-3,4)
y = np.zeros(len(x))

for i in range(0,len(x)):  # Esto es para generar funciones punto por punto. 
    y[i] = 2 - x[i]**2 

plt.plot(x,y,"s-")
plt.show()



# ------ 
x = np.linspace(-3,3,10) # Esta funcion es para ir del -3 al 3  en 10 pasos.   Crea puntos en la grafica. Asarosamente. 
y = 2 + np.sqrt(abs(x))

plt.plot(x,y,"ms-")
plt.grid()
plt.show()

# ---

x = np.linspace(-3,3,10) # Esta funcion es para ir del -3 al 3  en 10 pasos.   Crea puntos en la grafica. Asarosamente. 
y1 = 2 + abs(x)**(1/4)
y2 = 2 + abs(x)**(1/3)

plt.plot(x,y1,"m-")
plt.plot(x,y2,"k-")
plt.grid()
plt.show()


#----- exercise

x = np.linspace(-4,5,200)
poto = range(-1,4)
for i in poto:
    y = x**i
    plt.plot(x,y,linewidth = 4, label = " $y = x^{%s}$" % i )
    
plt.xlim(x[0],x[-1])
plt.ylim(-20,20)
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.show()


'''---------------------------------------------------------------------------------------------------------------------- 58'''
# Plotting with sympy
x = sym.symbols("x")  # Esto es necesario. Creo que a veces sobreescribimos la variable x y obtiene otro valor diferente. 
y = x**2

p = sym.plotting.plot(y, show = False)  # Con este metodo podemos graficar mucho mas rapido. Sin darle valores a las "x"

p[0].line_color = "m"  #Aqui es para cambie el color de una sola cosa. 
p.ylim = [0,50]        # Para delimitar el eje y
p.xlim = [0,50]        # Para delimitar el eje x
p.title = "This is a nice plot!"

p.show()



#------------------------

import sympy.plotting.plot as symplot   # Esto es para abreviar todo el codigo. 


x,a = sym.symbols("x,a")
expr = a/x
n = 1

p = symplot(expr.subs(a,n), (x,-5,5), show = False)  # Primero le damos un valor a "a" para que el programa tenga la suficiente informacion para graficar
                                       # Despues entre parentesis ponermos que variable queremos delimitar. -->  x  de -5 a 5
                                    
# p[0].label = "$y = \\frac{%s}{x}$" %  n #Esto es para la etiqueta  --> Una opcion. 
p[0].label = "$y = %s$" %  sym.latex(expr.subs(a,n))   # Esto es para la etiqueta  --> otra opcion. 

p2 = symplot(expr.subs(a,3), (x,-5,5), show = False)
p2[0].label = "$y = %s$" %  sym.latex(expr.subs(a,3))# Creo que si tienen el mismo limite puede que cambien de color. (suposicion)
p.extend(p2)

p.ylim = [-5,5]
p.legend = True
p.show()


'''--------------------------------------------------------------------------------------------------------------------- 59'''

# --- Exercise

# Mi intento 

g = symplot()
for i in range(1,5):
    a = i
    y = a/(x**2 -a)
    g.extend(symplot(y,(x,-5,5), show = False))
    g.label = "$ %s $" % sym.latex(y)
    
    
g.ylim = [-10,10]
g.legend = True
g.show()


# ---- Del profesor

y = a/(x**2 -a)

p = None   # Esto es para quitar cualquier valor que "p" haya tenido
p = symplot(y.subs(a,1), (x,-5,5), show = False)
p[0].label = "$ %s $" % sym.latex(y.subs(a,1))

for i in range(2,5):
    p.extend(symplot(y.subs(a,i), (x,-5,5), show = False))
    p[i-1].label = "$ %s $" % sym.latex(y.subs(a,i))
    p[i-1].line_color = np.random.rand(3) # Esto es para generar numeros aleatoriamente.   Puede ser que necesitemos poner todo esto en una lista. "list(np.random.rand(3))"
    
    
p.ylim = [-10,10]
p.legend = True
p.show()

'''---------------------------------------------------------------------------------------------------------------------- 61'''
# Making images from matrices 

# We need to know this formula  --> ai,j  = 3*i - 4*j

A = [ [1,2], [1,4]]

plt.imshow(A) # Esto es para mostrar la matris con colores. 
plt.xticks([0,1])
plt.yticks([0,1])
plt.show()


#------------

A = np.zeros((10,14))

for i in range(0, np.shape(A)[0]):
    for j in range(0,np.shape(A)[1]):
        A[i,j] = 3*i - 4*j
        
print(A)
plt.imshow(A)

plt.plot([0,12], [9,1], "r", linewidth = 4)

for i in range(0, np.shape(A)[0]):
    for j in range(0,np.shape(A)[1]):
        plt.text(j,i,int(A[i,j]), horizontalalignment = 'center', verticalalignment = 'center')
        
plt.set_cmap('binary')

plt.show()



'''----------------------------------------------------------------------------------------------------------------------- 62'''
# Exercise
# c[i,j] = -1 ^ i+j

N = 10
A = np.zeros((N,N))

for i in range(0,N):
    for j in range(0,N):
        A[i,j] = (-1) ** (i+j)  # Cuidado con los parentesis. 

print(A) 

plt.imshow(A)
plt.tick_params(labelleft = False, labelbottom = False)
plt.show()


'''----------------------------------------------------------------------------------------------------------------------- 63'''
# Drawing patches with polygons. 

plt.plot(1,4,"oc")
plt.plot(1,1,"oc")
plt.plot(4,1,"oc")
plt.grid()
plt.axis("square")
plt.xlim([0,5])
plt.ylim([0,5])
plt.show()

# ---------------------
from matplotlib.patches import Polygon  # Necesitamos esto 

y = np.array([ [1,1] , [2,3] , [3,1] ])  # esto es una matris 
P = Polygon(y, facecolor = "b", alpha = .5, edgecolor = 'p') # alpha es para cambiar la transparencia de la figura. 

y1 = np.array([ [2,2] , [2.5,4] , [3.5,1] ])  # esto es una matris 
P1 = Polygon(y1, facecolor = "y", alpha = .5, edgecolor = "r") # alpha es para cambiar la transparencia de la figura. El rango varia entre 0 y 1


fig , ax = plt.subplots() # Todavia no se para que sirve esta funcion. 

ax.add_patch(P)
ax.add_patch(P1)
ax.set_ylim([0,4])  # debes de tener cuidado con los limites. Puede que no se llegue a ver la figura. 
ax.set_xlim([0,4])
plt.show()

# ----- Exercise
x = np.linspace(-2,2,100) #funcion para ir del -2 al 2 en 100 puntos
f = -x**2

y = np.vstack((x,f)).T  # este metodo es para hacer un matris     -->  el ( .T ) es para intercabmiar las columnas y las filas. 
y1 = np.array([ [-.5, -4], [.5, -4] ,[.5,-2.5] , [-.5, -2.5]]) # este es el cuadrado 

P = Polygon(y, facecolor = "g", alpha = .2)
P1 = Polygon(y1, facecolor = "k", alpha = 1)

fig , ax = plt.subplots()

plt.plot(x,f, 'k') # Esto el profesor lo uso para crear el borde. en realidad es unalinea negra. 
plt.plot([-2,2], [-4,-4], "k") # Esto es una simple linea. Aparenta ser un borde. 
plt.axis('off') # Esto es para quitar la tabla. 

ax.add_patch(P)
ax.add_patch(P1)
# ax.set_xlim([-2,2])
# ax.set_ylim([-4,0])  # el primer numero es el numero que ira mas cerca del la esquina izquierda. 

plt.show()

'''---------------------------------------------------------------------------------------------------------------------- 64'''
# Exporting graphics as pictures. 

plt.savefig("ThisIsANiceFigure.png")   # podemos guardar como png, pdf,jpg, 

''' ---------------------------------------------------------------------------------------------------------------------- 65'''
# Bug hunt

plt.plot(3,2,'ro')

plt.axis('square')
# plt.axis([-6,6,-6,6])  -->  Este metodo tamgbien sirve y hace lo mismo. 
plt.xlim([-6,6])
plt.ylim([-6,6])
plt.show()

#--------------

plt.plot([0,3], [0,5])
plt.show()

#--------------

x = range(-3,4)
y = np.zeros([len(x) , len(x)])

for i in range(0, len(x)):
    y[i] = 2 - x[i]**2
    
plt.plot(x,y, "s-")
plt.show()

# ------------ 

plt.plot([-2,3], [4,0],'b')
plt.plot([0,3], [-3,3],'r')

#plt.legend()
plt.show()

#-------------

randmat = np.random.randn(5,9)
plt.plot([0,4],[8,0], color = (.4,.1,.9), linewidth = 5)

plt.imshow(randmat)
plt.set_cmap('Purples')
plt.show()

#-------------

plt.plot([-2,3], [4,0],'b', label = 'line1')
plt.plot([0,3], [-3,3],'r', label = 'line2')

plt.legend()
plt.show()

#------------

x = np.linspace(1,4,20)
y = (x**2)/(x-2)

plt.plot(x,y)

#-------------

x = sym.symbols('x')
y = x**2 - 3*x

xrange= range(-10,11)

for i in range(0,len(xrange)):
    plt.plot(xrange[i], y.subs(x,xrange[i]), 'o')

plt.xlabel('x')
plt.ylabel("$ f(x) = %s $" % sym.latex(y))
plt.show()
    
#-------------

x = [-5,5]
m = 2
b = 1

y = m*np.array(x) + b

plt.plot(x,y)
plt.show()

#-------------

x = range(-20,121)

for i in range(0, len(x)):
    plt.plot([0, x[i]] , [0, abs(x[i])**(1/2)], color = (i/len(x), i/len(x), i/len(x)))

plt.axis("off")
plt.show()

#------------

m = 8 
n = 4

c = np.zeros((m,n))

for i in range(0,m):
    for j in range(0,n):
        c[i,j] = (-1) **(i+j)

for i in range(0, m):
    for j in range(0, n):
        plt.text(j,i,i+j, horizontalalignment = "center", verticalalignment = "center", fontdict=dict(color = "m"))


plt.imshow(c)
plt.set_cmap("gray")
plt.show()





