from socket import IPV6_LEAVE_GROUP
import sympy as sym
import matplotlib.pyplot as plt 
from sympy.abc import w,x,y,z,g,t
import numpy as np
from IPython.display import display, Math



'''-------------------------------------------------------------------------------------------------------------------- 111'''
# Ateroid radical curve. 

t = np.linspace(-6*np.pi, 6*np.pi, 1000)
a = t


x = a * np.cos(t)**3
y = a * np.sin(t)**3

plt.plot(x,y,'m', linewidth = 3)
plt.axis("square")
plt.axis('off')

plt.show()

# exercise


fig , ax = plt.subplots(3,3, figsize = (10,6))
row , col = np.indices((3,3)) # Esto es para crear una dos matrices (en este caso)

for i in range(9):
    a = t**i

    x = a * np.cos(t)**3
    y = a * np.sin(t)**3
    
    r = row.ravel()[i]
    c = col.ravel()[i]
    
    ax[r,c].plot(x,y)
    ax[r,c].axis('off')
    ax[r,c].axis("square")
   
    
plt.show()


'''------------------------------------------------------------------------------------------------------------------- 112'''
# roses curves

k1 = 2

t1 = np.linspace(0, 12*np.pi, 1000)

x1 = np.cos(k1*t1)*np.cos(t1)
y1 = np.cos(k1*t1)*np.sin(t1)

plt.plot(x1,y1, 'g' , linewidth = 3)

plt.axis("square")
plt.axis("off")
plt.show()


# exercise

fig,ax = plt.subplots(3,3)

row,col = np.indices((3,3))

for i in range(9):
    k1 = i/2
    t1 = np.linspace(0, 8*np.pi, 1000)

    x1 = np.cos(k1*t1)*np.cos(t1)
    y1 = np.cos(k1*t1)*np.sin(t1)
    
    r = row.ravel()[i]
    c = col.ravel()[i]
    

    ax[r,c].plot(x1,y1)
    ax[r,c].axis("square")
    ax[r,c].axis("off")
    ax[r,c].set_title("k=%s" % (k1))

plt.legend()
plt.show()


'''--------------------------------------------------------------------------------------------------------------------113'''
# Squircle

a = 1
y = np.linspace(-1,1,2000)
x = (a**4 - y**4)**(1/4)


plt.plot(x,y,'k', linewidth = 5)
plt.plot(-x,y,'k', linewidth = 5)

plt.axis("square")
plt.axis("off")
plt.show()

'''---------------------------------------------------------------------------------------------------------------------114'''
# Logarithmic spiral

t = np.linspace(0,10*np.pi,1000)
k = -3

x = np.cos(t)*np.exp(t/k)
y = np.sin(t)*np.exp(t/k)

plt.plot(x,y)

plt.axis("square")
plt.show()



# exercise

N = 150
ks = np.linspace(-6,-2, N)

for i in range(N):

    x = np.cos(t)*np.exp(t/ks[i])
    y = np.sin(t)*np.exp(t/ks[i])

    plt.plot(x,y, color = [0,i/N, i/N] )

plt.axis("square")
plt.show()


'''----------------------------------------------------------------------------------------------------------------------115'''
# Logistic Map
















































































