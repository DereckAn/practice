
from cProfile import label
from socket import IPV6_LEAVE_GROUP
import sympy as sym
import matplotlib.pyplot as plt 
from sympy.abc import w,x,y,z,g,t
import math
import numpy as np
from IPython.display import display, Math
import scipy as sp


'''---------------------------------------------------------------------------------------------------------------------- 67'''
#Summation and products

lst = [1,3,4,1,6]
print(sum(lst)) # Metodo para hacer la sumatoria
print(np.sum(lst))  # Metodo para hacer la sumatoria 
print(np.prod(lst)) # Metodo para obtener el producto.  (pi mayuscula)
print(np.cumsum(lst)) # Metodo para obtener la sumatoria acumulada. 

plt.plot(lst, "rs-")
plt.plot(np.cumsum(lst), "bo-")
plt.plot(np.sum(lst), "go-")

plt.legend(["set", "Cumsum"])
plt.show()

# ------------------- Exercise
#mio
alo = [1,2,3,4,5]

# print(np.sum(alo)/np.sum(alo**2) == 1 / np.sum(alo))

print(np.sum(alo)/((np.sum(alo))**2) == 1 / np.sum(alo))

# print(np.prod(alo) / np.prod(alo**2) == 1 / np.prod(alo))

print(np.prod(alo) / ((np.prod(alo))**2) == 1 / np.prod(alo))

##-- profe 

a = np.arange(1,6)
suma = np.sum(a)
suma2 = np.sum(a**2)

ans1 = suma / suma2
ans2 = 1 / suma

print("Option 1 = %s" % ans1)
print("Option 2 = %s" % ans2)


prodd = np.prod(a)
prodd2 = np.prod(a**2)

ans1 = prodd / prodd2
ans2 = 1 / prodd

print("Option 1 = %s" % ans1)
print("Option 2 = %s" % ans2)


'''---------------------------------------------------------------------------------------------------------------------- 68'''
# Differences (Discrete derivative)
# Discrete difference operator = discrete derivative

#Yt = Xt+1 - Xt

x = [1,3,4,-4]

np.diff(x)  # Con este metodo restamos los valores.  el 1er valor menos el 2do, el 2do menos el 3ro, el 3ro menso el 4to, Y asi susecivamente. 

v = np.arange(0,10)
print(v)  # [0 1 2 3 4 5 6 7 8 9]
print(np.diff(v))  # [1 1 1 1 1 1 1 1 1]
print(np.diff(v,2)) #[0 0 0 0 0 0 0 0]  Lo que hace este metodo saca la diferencia de la diferencia. Saca la diferencia dos veces. 
print(np.diff(np.diff(v))) #[0 0 0 0 0 0 0 0] Este metodo hace lo mismo que el mentodo anterior, en la linea 74

#------- Exercise

#Este es un intento mio y fiunciona pero la grafica es diferente. El eje esta en el centro y lo que necesito es el eje en la parte baja izquierda. 
x = sym.symbols("x")
y = x**2
p = sym.plotting.plot(y, show = False)

p[0].line_color = 'b'
p.ylim = [-1,2]
p.xlim = [-2,2]
p.show()

# Otro intento mio 

x = np.linspace(-2,2,200) # Esta funcion es para ir del -3 al 3  en 10 pasos.   Crea puntos en la grafica. Asarosamente. 
f = x**2
df = np.diff(f)
dx = np.diff(x)

plt.plot(x,f,"-", label = 'f')
plt.plot(x[:-1],df/dx, 'r-', label= "df/dx")

plt.ylim([-1,2])
plt.xlim([-2,2])
plt.legend()
plt.grid()
plt.show()

'''--------------------------------------------------------------------------------------------------------------------- 69'''
# Roots of polynomials

## The polynomial
# 3x^2 + 2x - 1 = 0

coefs = [3,2,-1]  # El orden importa demasiado. Ten cuidado. 

roots = np.roots(coefs) # Este metodo es para encontrar las solucion al polinomio. 
print(roots)
x = sym.symbols("x")
pn = 3*x**2 + 2*x - 1

for i in roots:
    display(Math("\\text{At} x=%s,\\quad  %s = %s" % (i,sym.latex(pn), pn.subs(x,i))))

'''----------------------------------------------------------------------------------------------------------------------- 70'''
#Exercise 

#Mi intento -- pero no le entendi muy bien al ejercicio. 
p = 10
pol = range(0,p+1)
for i in pol:
    print(f"A degree - {i} polynomial has {i} roots" )


# Profesor
for i in range(1,11):
    coefs = np.arange(1, i+1)
    print(f"A degree-{len(coefs)-1} polynomial has {len(np.roots(coefs))} roots ")
    
print(coefs)

'''----------------------------------------------------------------------------------------------------------------------- 71'''
# The quadratic ecuation

a = 2
b = 7
c = 5
quadeqp = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
quadeqn = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
print(quadeqp,  quadeqn)


a = 3
b = 7
c = 5
quadeqp = (-b + np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Este metodo es para obtener los valores imaginarios. 
quadeqn = (-b - np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Hubo varios pedos aqui. Se actualizo el formato scipy.
print(quadeqp,  quadeqn)


def quadeq(a,b,c):
    
    out = np.zeros(2)
    
    out[0] = (-b + np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Este metodo es para obtener los valores imaginarios. 
    out[1] = (-b - np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Hubo varios pedos aqui. Se actualizo el formato scipy.
    
    return out

print(quadeq(2,7,5))

# --------  Exercise

a = 1
b = range(-5,6)
c = range(-2,11)


A = np.zeros((len(b), len(c)))


for i in b:
    for j in c:
        
        A[i,j] = (-(i) + np.lib.scimath.sqrt(i**2 - 4*a*j)) / (2*a)
        
plt.imshow(A)

#------------- 

a = 1
b = range(-5,6)
c = range(-2,11)

def quadeq(a,b,c):
    
    out = np.zeros(2)
    
    out[0] = (-b + np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Este metodo es para obtener los valores imaginarios. 
    out[1] = (-b - np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Hubo varios pedos aqui. Se actualizo el formato scipy.
    
    return out

A = np.zeros((len(b), len(c)))

for i in range(0,len(b)):
    for j in range(0,len(c)):
        A[i,j] = quadeq(a,b[i],c[j])[0]

plt.imshow(A, extent = [c[0],c[-1], b[0],b[-1]])
# plt.set_cmap('Paired')
plt.ylabel('c')
plt.xlabel('b')
plt.title('a= ' + str(a))
plt.colorbar()
plt.show()

'''----------------------------------------------------------------------------------------------------------------------- 72'''
# Complex numbers: addition and subtraction. 

# z = a bi

# z = complex number
# a = Real part
# b = Imaginary part
# i = Imaginary Operator


print(1j)
print(np.sqrt(-1))
print(np.sqrt(-1, dtype="complex")) # Esta es otra manera para mostrar los numeros complejos. 
print( (-1)**(1/2) ) # Esta es otra manera para mostrar los numeros complejos. 
print(sym.I) # Esta 'I' se usa en el modulo simpy para representar los numeros complejos. 
print(np.lib.scimath.sqrt(-1)) # Metodo para mostrar los valoresimaginarios o complejos. 



real_part = 4
imag_part = 5

# cn1 = np.complex(real_part, imag_part)  # Esta manera esta descontinuada. Solo tienes que escribir 'complex' o 'np.complex128'
cn1 = complex(real_part, imag_part)  # Manera para sumar o restar numeros complejos.
cn2 = real_part + imag_part*1j # Otra manera para restar o sumar numeros complejos. 

print(cn1)
print(cn2)


# sumar o restar

z1 = complex(4,5)   # Aqui aplique los dos metodos para representar los numeros complejos. 
z2 = 3 + 2*1j

print(z1+z2)

np.real(z1)  # Este es para mostrar SOLO el numero real.
np.imag(z1)  # Este es para mostrar SOLO el numero imaginario. 


#------------------------------------------ Exercise

w = 2 + 4*1j
z = 5 + 6*1j
holaaaa = complex(np.real(w) + np.real(z), np.imag(w)+np.imag(z)) # Esta es otra manera para sumera numeros complejos. Pero es muy larga
holaaaa2 = w + z
print(holaaaa)
print(holaaaa2)

'''----------------------------------------------------------------------------------------------------------------------- 73'''
# Complex Numbers: Conjugate and multiplication. 

z1 = 4 + 5*1j
z2 = complex(6,-2)

print(z1*z2) #(34+22j)
sym.sympify(z1*z2) # 34 + 22i

np.conj(z1)  #(4-5j)


#-------- Exercise 
a,b = sym.symbols("a,b", real =  True)

z3 = a + b*sym.I

sym.conjugate(z3) 

z3 * sym.conjugate(z3)
display(Math(sym.latex(sym.expand(z3 * sym.conjugate(z3))))) # Para aplicar la propiedad distributiva usamos el 'sym.expand()'

'''---------------------------------------------------------------------------------------------------------------------- 74'''
# Complex Numbers: Division

z4 = 4 + 2*1j
z5 = 2 - 3*1j

display(Math("\\frac{%s}{2} = %s" % (z4,z4/2)))

display(Math("\\frac{%s}{%s} =  \\frac{%s \\times %s}{ %s \\times %s} = %s" \
             % (z4,z5, \
                z4,np.conj(z5), z5, np.conj(z5), \
                z4/z5)))

# ---- Exercise
# mi intento
z,w = sym.symbols("z,w")
z = 4 + 2*1j
w = 3 + 5*1j

ecuat1 = ((z-1)*(z*w + w))/( w*z - w)
ecuat2 = ((w-1)*(1-w))/(-z*w**2 - w**2 + 2*w*z + 2*w - z - 1)

ecuatFin = ecuat1 * ecuat2

display(Math("\\frac{(z-1)(zw + w)}{wz - w} \\times \\frac{(w-1)(1-w)}{-zw^2 - w^2 + 2wz + 2w - z - 1}"))

display(Math("%s \\times %s = %s" % (sym.latex(ecuat1), sym.latex(ecuat2), ecuatFin)))

# -------- - profesor
z= complex(4,2)
w = complex(3,5)

left_numer = (z-1)*(z*w + w)
left_denom = ( w*z - w)
left_part = left_numer / left_denom

right_numer = (w-1)*(1-w)
right_denom = (-z*w**2 - w**2 + 2*w*z + 2*w - z - 1)
right_part = right_numer / right_denom

solution = left_part * right_part

print(solution)


'''---------------------------------------------------------------------------------------------------------------------- 75'''
# Graphing complex numbers. 

z = 2 + 3*1j

plt.plot(np.real(z), np.imag(z), "ro")
plt.plot([0,np.real(z)], [0,np.imag(z)], 'r')
plt.xlabel("real")
plt.ylabel("imag")
plt.grid()
plt.axis([-4,4,-4,4])
plt.show()


# exercise. 
# mi intento 

z1 = -3 + 1*1j 
z2 = -1 + 1*1j

z3 = z1 + z2

plt.plot([0,np.real(z1)], [0, np.imag(z1)], label = "z1")
plt.plot([0,np.real(z2)], [0, np.imag(z2)], label = "z2")
plt.plot([0,np.real(z3)], [0, np.imag(z3)], label = "z1+z2")

plt.xlabel("real")
plt.ylabel('imag')
plt.grid()
plt.legend()
plt.axis('square')
plt.axis([-4,4,-4,4])
plt.show()

'''---------------------------------------------------------------------------------------------------------------------- 76'''
#Revisisitn the quadratic equation with complex numbers. 

a = 1
b = range(-5,6)
c = range(-2,11)

def quadeq(a,b,c):
    
    out = np.zeros(2)
    
    out[0] = (-b + np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Este metodo es para obtener los valores imaginarios. 
    out[1] = (-b - np.lib.scimath.sqrt(b**2 - 4*a*c)) / (2*a)  # Hubo varios pedos aqui. Se actualizo el formato scipy.
    
    return out

A = np.zeros((len(b), len(c)), dtype = complex)

for i in range(0,len(b)):
    for j in range(0,len(c)):
        A[i,j] = quadeq(a,b[i],c[j])[0]


plt.subplot(1,3,1) # Este metodo es para hacer como una lista o matris de graficas. 
plt.imshow(np.real(A), extent = [c[0],c[-1], b[0],b[-1]])
# plt.set_cmap('Paired')
plt.axis('off')
plt.title('Real part')
#plt.colorbar()



plt.subplot(1,3,2)
plt.imshow(np.imag(A), extent = [c[0],c[-1], b[0],b[-1]])
# plt.set_cmap('Paired')
plt.axis('off')
plt.title('Imag part')
# plt.colorbar()



plt.subplot(1,3,3)
plt.imshow(np.absolute(A), extent = [c[0],c[-1], b[0],b[-1]])
# plt.set_cmap('Paired')
plt.axis('off')
plt.title('Absolute part')
# plt.colorbar()
plt.show()


# Aqui hay un codigo que necesito averiguar bien. 


'''---------------------------------------------------------------------------------------------------------------------- 77 '''
# The unite circle. 

x = np.linspace(0, 2*np.pi, 100)

plt.plot(np.cos(x), np.sin(x), 'k')
plt.plot([-1.1,1.1], [0,0], '--', color = [.8,.8,.8])
plt.plot([0,0], [ -1.1, 1.1], '--', color = [.8,.8,.8])

angle = np.pi/4
plt.plot([0,np.cos(angle)], [0,np.sin(angle)])

plt.axis('square')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.xlabel('cos(x)')
plt.ylabel('sin(x)')

plt.show()


# ---------------- Exercise

x = np.linspace(-3,1.83, 50)
k = np.exp(x)  # Esto es lo mismo que esto -->  e^x


for i in k:
    plt.plot([0,np.cos(i)], [0,np.sin(i)])

plt.axis('square')  
plt.axis('off')

plt.show()

'''----------------------------------------------------------------------------------------------------------------------- 78'''
# Natural exponents and logarithms. 
 
x = np.linspace(-3,3,99)

plt.plot(x, np.exp(x))
plt.xlabel('x')
plt.ylabel('$e^x$')
plt.show()

plt.plot(x, np.log(x))
plt.xlabel('x')
plt.ylabel('log(x')
plt.show()

# Exercise
x = np.linspace(0.0001, 10, 10)
y1 = np.log(np.exp(x))
y2 = np.exp(np.log(x))


plt.plot(x, y1, label= "$log(e^x)$")
plt.plot(x, y2, 'o', label= "$e^{log(x)}$")

plt.axis('square')
plt.legend()
plt.show()


'''---------------------------------------------------------------------------------------------------------------------- 79'''
#  Find a specific point on a Gaussian 
h = .999
t = np.linspace(-3,3,1001)

g = np.exp(  -4*np.log(2)*t**2  / h**2)

plt.plot(t,g)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Gaussina wiht FWHM=' + str(h))
plt.show()

yVal2Find = .5
tVal = h*np.sqrt( np.log(yVal2Find)/(-4*np.log(2)))
print(tVal, -tVal)

# Exercise ------------------------------------------------------ 80 

N = 100
G = np.zeros((N, len(t)))
h = np.zeros(N)

for i in range(N):
    h[i] = (i+1)/N  # Ponemos el uno para que no tengamos que dividir 0
    G[i,:] = np.exp(-4*np.log(2)*t**2  / h[i]**2)  

plt.pcolormesh(t,h,G)
plt.xlabel('t')
plt.ylabel('h')
plt.show()

# Tengo que volver a ver este video porque no entendi lo que teneiamos que ahcer en el video. 

'''-------------------------------------------------------------------------------------------------------------------- 81'''
# Graphing the complex roots of unity

# z^n = 1      z e C
# z = e ^ 2pi i k / n   
# k = 0,1,2,3, ... n-1


n = 5

for k in range(0,n):
    z = np.exp(2*np.pi*1j*k / n)
    print(z**n)



n = 5

for k in range(0,n):
    z = sym.exp(2*sym.pi*sym.I*k / n)
    display(Math("(%s)^{%s} \\Rightarrow %s " % (sym.latex(z),n, sym.latex(z**n))))


n = 4 
for k in range(0,n):
    z = np.exp(2*np.pi*1j*k / n)
    plt.plot([0,np.real(z)] , [0,np.imag(z)])
    
x = np.linspace(0,2*np.pi, 100)
plt.plot(np.cos(x), np.sin(x), color = 'gray')
plt.axis('square')


plt.show()


# ---------------- exercise

n = 100
colorr = np.linspace(0,.9, n)
for k in range(0,n):
    z = k*np.exp(2*np.pi*1j*k / n)
    plt.plot([0,np.real(z)] , [0,np.imag(z)], linewidth = 2, color = [colorr[k], colorr[k], colorr[k]])

plt.axis('square')
plt.axis('off')
plt.show()

'''--------------------------------------------------------------------------------------------------------------------- 82'''
# log-spaced and linearly spaced numbers. 

# linear = 1,2,3,4,5,6,7
# log-space = 1, 1.5 ,2.2 , 3.3 , 5 

np.linspace(1,5,10)

np.logspace(1,2,10) #array([ 10,  12.91549665,  16.68100537,  21.5443469 , 27.82559402,  35.93813664,  46.41588834,  59.94842503, 77.42636827, 100.        ])

np.logspace(np.log10(1), np.log10(2), 10) # array([1, 1.08005974, 1.16652904, 1.25992105, 1.36079   , 1.46973449, 1.58740105, 1.71448797, 1.85174942, 2.        ])

# ---------- exercise
# mio
# Esta mal
a = -1
b = 2

y = np.logspace(a,b, 101)
x = np.linspace(0,100,101)
plt.plot(y, label = "log")
plt.plot(x,x, label =' linear')


plt.axis('square')
plt.legend()
plt.show()

# -- intento del profesor

a = 2
b = 100
n = 50

li = np.linspace(a,b,n)
lo = np.logspace(np.log10(a), np.log10(b), n)

plt.plot(li,li, label= 'linear')
plt.plot(li,lo,label='log')

plt.legend()
plt.axis('square')
plt.show()

'''--------------------------------------------------------------------------------------------------------------------- 83'''
# Logarithm properties: Multiplication and division. 

a = 3
b = 4

res1 = np.log(a*b)
res2 = np.log(a) * np.log(b)
res3 = np.log(a) + np.log(b)

display(Math('\\log(%g\\times%g) = %g ' % (a,b,res1)))
display(Math('\\log(%g)\\times\\log(%g) = %g ' % (a,b,res2)))
display(Math('\\log(%g)+\\log(%g) = %g ' % (a,b,res3)))

display(Math('\\log(%g\\times%g) = \\log(%g)+\\log(%g)' % (a,b,a,b)))
display(Math('\\log(%g\\times%g) \\neq \\log(%g) \\times \\log(%g)' % (a,b,a,b)))



res1 = np.log(a/b)
res2 = np.log(a) / np.log(b)
res3 = np.log(a) - np.log(b)

display(Math('\\log \\left( \\frac{%g}{%g} \\right) = %g ' % (a,b,res1)))
display(Math('\\log(%g)/\\log(%g) = %g ' % (a,b,res2)))
display(Math('\\log(%g)-\\log(%g) = %g ' % (a,b,res3)))

display(Math('\\log \\left( \\frac{%g}{%g} \\right) = \\log(%g)-\\log(%g)' % (a,b,a,b)))
display(Math('\\log \\left( \\frac{%g}{%g} \\right) \\neq \\frac{\\log(%g)}{\\log(%g)}' % (a,b,a,b)))


# ----- exercise

res1 = np.log(a**b)
res2 = np.log(a)**b
res3 = b*np.log(a)
display(Math("\\log \\left(%g ^{%g} \\right) = %g \\log \\left(%g\\right)" % (a,b,b,a)))

display(Math("\\log(%g^{%g}) = %g" % (a,b,res1)))
display(Math("\\log(%g)^{%g} = %g" % (a,b,res2)))
display(Math("%g\\log(%g) = %g " % (a,b,res3) ))


'''----------------------------------------------------------------------------------------------------------------------84'''
# Arithmetich and geometric sequences. 
# las secuancias aritmeticas crecen mas lento, creo que porque van sumando 
# las secuancias geometricas crecen mucho mas rapido porque se van multiplicando o tienen exponenetes. 

# parameters 
a = 2
d = 3
maxn = 6

ariseq = a + d*np.arange(0,maxn)

print(ariseq) #[ 2  5  8 11 14 17 20 23 26 29]



a = 2
r = 3

geoseq = a * r**np.arange(0,maxn)
print(geoseq) # [    2     6    18    54   162   486  1458  4374 13122 39366]


plt.plot(ariseq, 'ks', label = 'arithmetic')
plt.plot(geoseq, 'ro', label = 'geometric')


plt.legend()
plt.show()


# Exercises 

a = 2
d = 3
maxn = 10
nth = 6

ariseq = a + d*np.arange(0,maxn)
geoseq = a * d**np.arange(0,maxn)

# direct computation. 
ariDirect = a + d*(nth-1)
geoDirect = a * d**(nth-1)

print(ariDirect, ariseq[nth-1])
print(geoDirect, geoseq[nth-1])


'''----------------------------------------------------------------------------------------------------------------------85'''
# Orders of magnitud and scientific notation 

# 10021 = 1x10**4   = 1e+04
# 2119 = 2x10**3    = 2e+03
# 0.034 = 3x10**-2  = 3e-02

x = 78984565123

'{:,e}'.format(x)  # Este codigo es para transformar el numero a notacion cientifica. --> '7.898457e+10'
'{:,d}'.format(x)  # Este codigo es para separa el numero con comas. --> '78,984,565,123'
'%s' % x  # Este es el codigo normal para remplazar valores en una cadena. 
'%e' % x # Este codigo es para remplazar el valor pero lo convierte en notacion cientifica. 
'%.2e' % x #Es lo mismo que el codigo de arriba pero con dos decimales de precision. 

# ------- Exercise
# Print the nearest oder of magnitud of a given number. 

# mi solucion si funciona  :)   Pero solo para numeros positivos y creo que no apra numeros con punto decimal. 
#a = int(input(print("Please enter a number")))
#print(f"{a} is {len(str(a)[1:])} orders of magnitud, {('{:,.1e}'.format(a))}")

# solucion del profesor.

num = 2342

orderOfMag = int(np.floor(np.log10(abs(num)))) # Este metodo tiene sus truquitos. Tienemos que redondear, usar logaritmos para y valor obsoluto para los numerso negativos. 

numstr = '{:,e}'.format(num)
wheredot = numstr.find('.')
scinot = numstr[:wheredot]

display(Math("%s \\text{ is } %s \\text{ orders of magnitud, } \\approx %s \\times 10^{%g}" % (num, orderOfMag, scinot, orderOfMag)))


'''----------------------------------------------------------------------------------------------------------------------86'''
# Maxima and minima functions. 

lsts = [-4,5.5,1,2]

maxVal = np.max(lsts) # Este codigo te dice cual es el numero mas alto de la lista. 
maxvalID = np.argmax(lsts) # Este metodo dice en que lugar el numero maximo esta en la lista.
lsts[maxvalID]  #--> 5.5






x = np.linspace(0, 2*np.pi, 20)
fx = -(np.cos(x) + np.sqrt(x))

fmax = np.max(fx)
fmaxID = np.argmax(fx)
print(fmax, fmaxID)

plt.plot(x,fx, 'bo-')
plt.plot(x[fmaxID], fmax, 'rs')
plt.show()



x = np.linspace(-2,2,51)
fx = x**3 + x**4

fminID = np.argmin(fx)

plt.plot(x,fx,'s-')
plt.plot(x[fminID], fx[fminID], 'rs')

plt.xlim([-1.2,.5])
plt.ylim([-.2, .2])
plt.show()


# ----- exercise
from scipy.signal import find_peaks


x = np.linspace(0,12*np.pi, 213)
fx = -np.cos(x) - np.sqrt(x)
 
peeks = find_peaks(fx)  # Nos regresa una tupla.  --> (array([ 15,  49,  82, 116, 149, 182], dtype=int64), {})
print(peeks[0])

plt.plot(x,fx)
plt.plot(x[peeks[0]], fx[peeks[0]], 'o')
plt.show()


'''---------------------------------------------------------------------------------------------------------------------87 '''
# Even and odd functions. 

x = np.linspace(-5,5,20)
fEven = x**2
fEvenneg = (-x)**2


plt.plot(x,fEven)
plt.plot(x, fEvenneg,'ro')
plt.show()



fOdd = x**3
fOddneg = (-x)**3
FNegodd = -fOdd

plt.plot(x,fOdd)
plt.plot(x,fOddneg,'ro')
plt.plot(x,FNegodd,'g')
plt.show()


# ------ exercise

x = np.linspace(-10,10, 111)
fsen = np.sin(x)
fsenneg = np.sin(-x)

plt.plot(x,fsen)
plt.plot(x,fsenneg,'rs')
plt.show()


fsen = np.cos(x)
fsenneg = np.cos(-x)

plt.plot(x,fsen)
plt.plot(x,fsenneg,'rs')
plt.show()

'''----------------------------------------------------------------------------------------------------------------------88'''
# Bug Hunt. 

lst = [1,3,4,1,5]
print(lst)


# -----------------

print(np.sum(lst)) 

# -----------------
l = np.arange(-4,10)

plt.plot(l,'rs-')
plt.plot(np.cumsum(l),'bo-')
plt.legend({'list', 'cumsum'})
plt.show()

# -----------------

coefs = [5,0,-2,4]

roots = np.roots(coefs)

from sympy.abc import x

p = sym.Poly(coefs, x)
display(Math(sym.latex(p)))


# -----------------

def quadeq (a,b,c):
    out = np.zeros(2, dtype = complex)
    out[0] = (-b + np.sqrt(b**2 - 4*a*c, dtype = complex)) / (2*a)
    out[1] = (-b - np.sqrt(b**2 - 4*a*c, dtype = complex) ) / (2*a)
    
    return out

print(quadeq(1,4,2))




def quadeq (a,b,c):
    
    out0 = (-b + np.sqrt(b**2 - 4*a*c, dtype = complex)) / (2*a)
    out1 = (-b - np.sqrt(b**2 - 4*a*c, dtype = complex) ) / (2*a)
    
    return [out0, out1]

print(quadeq(1,4,2))

# -----------------

real_part = 4
imag_part = -6

cn = complex(real_part, imag_part)

plt.plot(np.real(cn), np.imag(cn), 'ro')
plt.grid()
plt.axis('square')
plt.axis([-10,10,-10,10])
plt.show()


# -----------------

a,b = sym.symbols('a,b', real = True)

z = a + b *sym.I

display(Math("z\\times z^* = %s" % (sym.latex(sym.expand(z*sym.conjugate(z))))))

# -----------------

x = np.linspace(0,2*np.pi, 100)

plt.plot(np.cos(x), np.sin(x), 'k')

phs = 1*np.pi/4
plt.plot([0,np.cos(phs)], [0,np.sin(phs)], 'r-')
plt.plot(np.cos(phs), np.sin(phs), 'ro')

plt.plot([-1.3,1.3], [0,0], '--', color=[.8,.8,.8])
plt.plot([0,0],[-1.3,1.3], '--', color=[.8,.8,.8])

plt.axis('square')
plt.axis([-1.3,1.3,-1.3,1.3])
plt.ylabel('sin(x)')
plt.xlabel('cos(x)')
plt.show()

# -----------------

a = 2
b = 100
n = 3

li = np.linspace(a,b,n)
lo = np.logspace(np.log10(a), np.log10(b),n)

plt.plot(li,lo, 's-', label = "log")
plt.plot(li,li, 'o-', label = 'linear')

plt.legend()
plt.axis('square')
plt.show()

# -----------------

x = np.linspace(-6, 10, 20)

fx = 1/(1+np.exp(x))

fmaxid = np.argmin(abs(fx-.5))

plt.plot(x,fx,'bo-')
plt.plot(x[fmaxid], fx[fmaxid], 'rs')
plt.title("Sigmoid function.")
plt.show()


# -----------------

from scipy.signal import find_peaks

x = np.linspace(0, 12*np.pi, 200)

fx = -(np.cos(x) + x**(1/2))

peeks = find_peaks(-fx)  # ponemos la funcion en negativa para encontrar los puntos negativos. 


plt.plot(x,fx)
plt.plot(x[peeks[0]], fx[peeks[0]], 'o')
plt.show()





