from cProfile import label
import sympy as sym
import matplotlib.pyplot as plt 
from sympy.abc import w,x,y,z,g,t
import math
import numpy as np
from IPython.display import display, Math
import scipy as sp

'''--------------------------------------------------------------------------------------------------------------------- 90'''
# Graphing parabolas

# 4p(y-k) = (x-h)**2
# y = (1/4p)(x-h)**2 + k


a = 1
h = 1
k = -2
n = 100

x = np.linspace(h-5,h+5,n)

y = a*(x-h)**2 + k

plt.plot(y,x)
plt.axis('square')
plt.show()

#--------------  Exercise
p = 1/(4*a)
a = 1
h = 2
k = 1
n = 100
d = k-p

x = np.linspace(h-5,h+5,n)
y = a*(x-h)**2 + k

plt.plot(x,y, label = "Parabola")
plt.plot(h,k,"ro", label = "Vertex")
plt.plot(h,k+p,"go", label = "Focus")
plt.plot(x[[0,-1]],[d,d], label = "Directrix")

plt.axis([-6,6,0,10])
plt.legend()
plt.grid()
plt.show()


'''----------------------------------------------------------------------------------------------------------------------91'''
# Creating contours from meshes in Python. 

# Meshes is graphics. 

X,Y = np.meshgrid(range(0,10), range(0,15))

plt.subplot(121)
# plt.imshow(X)  
plt.pcolormesh(X, edgecolor = 'k', linewidth = .1) # Este codigo se aprece al anterior pero tiene un poco mas de variedad. 


plt.subplot(122)
plt.pcolormesh(Y,edgecolor = 'k', linewidth = .1)

plt.show()


# ----
x = np.linspace(-np.pi, 2*np.pi, 40)
y = np.linspace(0, 4*np.pi, 72)
X,Y = np.meshgrid(x,y)

Fxy = np.cos(X) + np.sin(Y)

# plt.imshow(Fxy)
plt.pcolormesh(Fxy, edgecolor = 'k')
plt.show()

#---------- Exercise
# 2D Gaussian 
x = np.linspace(-2,2,100)
X,Y = np.meshgrid(x,x)
s = 2
gauss2d = np.exp(-(X**2 + Y**2)/s)

plt.imshow(gauss2d)
plt.axis('off')
plt.show()

'''----------------------------------------------------------------------------------------------------------------------92'''
# Graphing circles. 
# (y-k)^2  +  (x-h)^2 = r^2

h = 2
k = -3
r = 3
axlim = r + np.max((abs(h), abs(k)))

x = np.linspace(-axlim,axlim,100)
X,Y = np.meshgrid(x,x)

Fxy = (X-h)**2 + (Y-k)**2 - r**2

# plt.imshow(Fxy)
# plt.contour(Fxy,0) # El '0' es para que solo muestra el primer circulo. ( el primer contour map)
plt.contour(X,Y,Fxy,0) # Y los 'X , Y' son para los limites de la grafica. 
plt.plot([-axlim, axlim], [0,0], 'k--')
plt.plot([0,0],[-axlim, axlim],  'k--')
plt.plot(h,k, 'go')
plt.gca().set_aspect('equal')

plt.show()

#---------- exercise

h = [-1.5,1.5]
x = np.linspace(-5,5.100)
X,Y = np.meshgrid(x,x) 


for r in np.linspace(.5,3,15):
    for hi in h:
        Fxy = (X-hi)**2 + Y**2 - r**2
        plt.contour(X,Y,Fxy,0, colors = [r/3,r/3,r/3])

plt.plot(h,[0,0],'k', linewidth = 3)
plt.axis('off')
plt.gca().set_aspect('equal')
plt.show()

# tengo que aprender como se usa el codigo   'np.meshgrip()'


'''----------------------------------------------------------------------------------------------------------------------93'''
# Graphing Ellipses 
# ((y-k)^2)/b^2  +  ((x-h)^2)/a^2 - 1 = 0

h = 1
k = 2
a = 2
b = 3 

axlim = np.max((abs(h) , abs(k))) + np.max((a,b))
x = np.linspace(-axlim, axlim , 100)
X,Y = np.meshgrid(x,x)

ellipse = (X-h)**2/(a**2) + (Y-k)**2/b**2 - 1

plt.contour(X,Y, ellipse, 0)
plt.plot(h,k,'go')
plt.plot([-axlim, axlim], [0,0], 'k--')
plt.plot([0,0],[-axlim, axlim],  'k--')
plt.gca().set_aspect('equal')


plt.show()

#---------- exercise
n = 16  # Esto tambien representara el numero de elipses. 
h = 0
k = np.linspace(-4,4,n)
a = abs(k)
b = 4

x = np.linspace(-8,8,100)

X,Y = np.meshgrid(x,x)


for i in range(0,n):
    F = (X-h)**2/a[i]**2 + (Y-k[i])**2/b**2  - 1
    plt.contour(X,Y,F,0, colors = [i/n, 0 , i/n])

plt.axis('off')
plt.gca().set_aspect('equal')

plt.show()
    
'''----------------------------------------------------------------------------------------------------------------------94'''
# Graphing hyperbolas. 
# ((y-k)^2)/b^2  -  ((x-h)^2)/a^2 - 1 = 0

a = 1 
b = .5
h = 1
k = 2
axlim = 2*np.max((a,b)) + np.max((abs(h), abs(k)))

x = np.linspace(-axlim, axlim,100)
X,Y = np.meshgrid(x,x)


hyoerbola = (X-h)**2/(a**2) - (Y-k)**2/b**2 - 1

plt.contour(X,Y,hyoerbola,0)
plt.plot(h,k,'go')
plt.plot([-axlim, axlim], [0,0], 'k--', color = [.8,.8,.8])
plt.plot([0,0],[-axlim, axlim],  'k--', color = [.8,.8,.8])
plt.gca().set_aspect('equal')
plt.show()

#------ exercise
n = 16
a = np.linspace(1,5,n)
b = a
h,k = 0,0
axlim = 8

x = np.linspace(-axlim, axlim,100)
X,Y = np.meshgrid(x,x)

for i in range(0,n):
    F1 = X**2/b[i]**2 - Y**2/a[i]**2 - 1
    plt.contour(X,Y,F1,0, colors =  [i/n, .8, i/n ])
    
    F2 = -X**2/b[i]**2 + Y**2/a[i]**2 - 1
    plt.contour(X,Y,F2,0, colors =[0, i/n, i/n])
    
plt.axis('off')
plt.gca().set_aspect('equal')

plt.show()
    
'''----------------------------------------------------------------------------------------------------------------------95'''
# Bug hunt

x = np.linspace(-2,2,100)

X,Y = np.meshgrid(x,x)
gauss2d = np.exp( -(X**2 + Y**2))

plt.imshow(gauss2d)
plt.axis('off')
plt.show()

# ---------
r = 3

x = np.linspace(-r,r,100)

X,Y = np.meshgrid(x,x)

Fxy = X**2 + Y**2 - r**2
plt.contour(Fxy,0)
# plt.imshow(Fxy)
plt.axis('off')
plt.axis('square')
plt.show()


# ------------
a = 1
b = 2
h = 2
k = -3 

axlim = np.max((a,b)) + np.max((abs(h), abs(k)))
x = np.linspace(-axlim, axlim, 100)
y = x 

X,Y = np.meshgrid(x,y)

Fxy = (X-h)**2/a**2 + (Y-k)**2/b**2 - 1

plt.contour(X,Y,Fxy,0)

plt.grid()
plt.title('Ellipse centered at (x,y) = (%s,%s)' % (h,k))
plt.gca().set_aspect('equal')
plt.show()

#----------
a = 1
b = .5
h = 1
k = 2 

axlim = 2*(np.max((a,b)) + np.max((abs(h), abs(k))))
x = np.linspace(-axlim, axlim, 100)
y = x 

X,Y = np.meshgrid(x,y)

Fxy = (X-h)**2/a**2 - (Y-k)**2/b**2 - 1

plt.contour(X,Y,Fxy,0)
plt.plot(h,k,'go')
plt.plot([-axlim, axlim], [0,0], '--', color = [.8,.8,.8])
plt.plot([0,0],[-axlim, axlim],  'k--', color = [.8,.8,.8])

plt.grid()
plt.title('Ellipse centered at (x,y) = (%s,%s)' % (h,k))
plt.gca().set_aspect('equal')
plt.show()




