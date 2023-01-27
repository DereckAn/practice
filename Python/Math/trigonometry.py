from random import random
from turtle import color
import matplotlib.pyplot as plt 
import numpy as np
import sympy as sym



'''---------------------------------------------------------------------------------------------------------------------97'''
# Introduction to random numbers. 


nums = np.random.rand(1000)  # el numero representa el numero de numerso aleatorios que noos regresara la computadora.  uniform distribution =. 
plt.plot(nums,'s')

minval = 2
maxval = 17

nums = nums*(maxval-minval) + minval
plt.show()

plt.hist(nums)
plt.show()


 
nums = np.random.randn(1000)  # Esta funcion da numeros aleatorios normales.    Solo cambia una letra.   Normal distribution 
plt.plot(nums,'s', alpha = .5)
plt.show()

plt.hist(nums)
plt.show()

'''----------------------------------------------------------------------------------------------------------------------98'''
# Exercise

desired_mean = 15
desired_std = 4.3

nums = np.random.randn(1000) #* desired_std  + desired_mean
nums = nums - np.mean(nums)  # Agregamos estos codigos para que el promedio sea exactamente lo que queramos. 
nums = nums / np.std(nums)  # Este codigo es para que tengamos la desviacion estandar que queremos. 

nums = nums*desired_std + desired_mean  # Agregamos estos codigos para que el promedio sea exactamente lo que queramos. 


plt.subplot(121)  #Este numero significa: 1 row - 2 colums - start in 1 subplot
plt.plot(nums, 's')

plt.subplot(122) #Este numero significa: 1 row - 2 colums - start in 2 subplot
plt.hist(nums)

plt.show()

print("This distribution has a mean of %s and a standar deviation of %s" % (np.mean(nums), np.std(nums)))

'''----------------------------------------------------------------------------------------------------------------------99'''
# Exercise: Plotting rando, phase angles. 

angs = np.random.randn(100)

for i in angs:
    plt.plot([0,np.cos(i)], [0,np.sin(i)])
    
plt.axis('square')
plt.axis([-1,1,-1,1])
plt.axis('off')
    
plt.show()

'''---------------------------------------------------------------------------------------------------------------------100'''
# Converting between radias and degrees

# rad = 360 / 2pi = 180/pi
# deg =2pi/360 = pi/180

deg = 180
rad = deg*np.pi/180
rad = rad%(2*np.pi) # Esto es para que no sea acumulativo. 

rad = np.deg2rad(deg) # esta funcion Sirve para convertir rapidamente grados a radianes. # Esta en la libreria numpy. \
    
print("%g degrees is %g radians" % (deg, rad  ))


rad = np.pi
deg = (180*rad/np.pi) % 360
deg = np.rad2deg(rad) # Este metodo ya viene el la librearia de numpy. 
print(deg)

'''---------------------------------------------------------------------------------------------------------------------101'''
# Converting angles: exercise

# My intento  -- creo que si funciona 
def angle_convert_plot():
    hola = True
    while hola:
        ang = float(input("What angle to convert?"))
        uni = input("Which unit did you input(radian or degree)?")
        if uni == "radian" or "r" or "R":
            plt.plot([0,np.cos(ang)],[0,np.sin(ang)],"r-")
            
        elif uni == "degree" or "d" or "D":
            deg = np.rad2deg(ang)
            plt.plot([0,np.cos(deg)],[0,np.sin(deg)],"r-")
        else:
            raise ValueError("Unknown unit!")
            
        
        plt.plot([0,1],[0,0],'r-')
        
        plt.title("Angle of %g, or %g rad." % (ang, np.deg2rad(ang)))
        plt.axis("square")
        plt.axis([-1,1,-1,1])
        plt.grid()
        plt.show()


angle_convert_plot()

# --- Intento del profesor 
# eval("1+2")  # El resultado sera 3
 
angle = eval(input("What angle to convert"))
unit = input("Wich unit did you input (degree or radian)?")

if unit[0].lower() == 'r':
    rad = angle
    deg = np.rad2deg(angle)
elif unit[0].lower() == 'd': 
    deg = angle
    rad = np.deg2rad(angle)
else:
    raise ValueError("Unkown Unit!")


# convert to <360
deg = deg%360
rad = rad%(2*np.pi)

plt.plot([0,1],[0,0],'r-', linewidth = 2)
plt.plot([0,np.cos(rad)],[0,np.sin(rad)],"r-")

plt.axis("square")
plt.axis([-1,1,-1,1])
plt.grid()
plt.title("Angle of %s$^o$, or %s rad." % (deg,rad))
plt.show()

'''-------------------------------------------------------------------------------------------------------------------- 102'''
# The pythagorean theorem. 

a = 3
b = 4

c = np.sqrt(a**2 + b**2)


plt.plot([0,a], [0,0], 'k', linewidth = 2)
plt.plot([0,0], [0,b], 'k', linewidth = 2)
plt.plot([0,a],[b,0]) 
plt.plot([.3, .3],[0,.3], 'k', linewidth = 1)
plt.plot([0, .3],[.3,.3], 'k', linewidth = 1)

plt.text(a/3,-.25,'a=' + str(a), fontsize = 13)
plt.text(.1, b/3, "b=" + str(b), fontsize = 13)
plt.text(a/2 + 1 ,b/2 , 'c=' + str(c), fontsize = 13)

plt.axis('square')
axlims = np.max((a,b)) + .5 
plt.axis([-.5,axlims,-.5,axlims])
plt.axis('off')
plt.show()


# exercise

z = complex(3,4)
mag1 = np.sqrt(np.real(z)**2 + np.imag(z)**2)
mag2 = abs(z) # En este caso este codigo hac elo mismo que el codigo de arriba (linea 176) 

print(mag1, mag2 )

ang1 = np.arctan2(np.imag(z), np.real(z))
ang2 = np.angle(z) # Este codigo saca el angulo de las coordenadas. HAce lo mismo que el codigo de arniba (linea 181)

print(ang1, ang2)


'''------------------------------------------------------------------------------------------------------------------ 103'''
# Graphing resolution for sine, cosine, and tangent


x = np.linspace(0,6*np.pi,400)
plt.plot(x,np.sin(x), 'r',label = "$\\sin(\\theta)$")
plt.plot(x,np.cos(x), 'g',label = "$\\cos(\\theta)$")

plt.legend()
plt.xlabel('rad')
plt.ylabel('function value')
plt.show()

th = np.linspace(0,4*np.pi, 300)
plt.plot(th,np.tan(th),'k')
plt.ylim([-5,5])
plt.show()

ang = np.random.rand()*2*np.pi
tann = np.tan(ang)
sc = np.sin(ang) / np.cos(ang)
print(ang , tann - sc)



# c^2 + s^2 = 1
thetas = np.linspace(0,2*np.pi,13)
print(thetas)
print(np.cos(thetas)**2 + np.sin(thetas)**2)

'''---------------------------------------------------------------------------------------------------------------------104'''
# Graphing and resolution: Exercises


# ejercicio 1 mio
x = np.linspace(0,6*np.pi,400)
y1 = np.sin(x + np.cos(x))
y2 = np.cos(x + np.sin(x))

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()

# ejercico 2 mio  // incompleto 
theta = (7*np.pi)/6

plt.plot(np.cos(x), np.sin(x))
plt.plot([0,np.cos(theta)],[0, np.sin(theta)],'--', color = 'lightgrey')
plt.plot([-1,1],[00,0], "--", color = 'lightgrey')
plt.plot([0,0],[-1,1], "--", color = 'lightgrey')

plt.axis("square")
plt.title('$\\theta = %s$' % (theta))
plt.show() 



# ejercicos que hixo el profesor 

x = np.linspace(-2*np.pi, 2*np.pi,200)
y1 = np.sin(x + np.cos(x))
y2 = np.cos(x + np.sin(x))

plt.plot(x,y1, x,y2)
plt.legend(['sin(x+cos(x))', "cos(x+sin(x))"])
plt.show()

# ------
thsym = sym.pi*7/6
theta = float(thsym)
x = np.linspace(0, 2*np.pi,200)

plt.plot(np.cos(x), np.sin(x))
plt.plot([-1,1],[0,0], "--", color = 'lightgrey')
plt.plot([0,0],[-1,1], "--", color = 'lightgrey')
plt.plot(np.cos(np.linspace(0,theta)), np.sin(np.linspace(0,theta)), 'k', linewidth = 3) # Este codigo es para hacer el arco. 
plt.plot([0,np.cos(theta)],[0, np.sin(theta)],'k:')
plt.plot([0,np.cos(theta)],[0, np.sin(theta)],'ko')
plt.plot([0,0], [0,np.sin(theta)],'r',label = "$\\sin(\\theta)$") # Esto es para las lineas de seno. Linea roja. 
plt.plot([0,np.cos(theta)], [0,0], 'g', label= "$\\cos(\\theta)$") # Este codigo es para obtener  los cosenos. Linea verde. 
plt.plot([0,np.cos(theta)],[np.sin(theta),np.sin(theta)],'g:')
plt.plot([np.cos(theta),np.cos(theta)],[0,np.sin(theta)],'r:')

plt.legend()
plt.title('$\\theta = %s$' % (sym.latex(sym.sympify(thsym))))
plt.axis("square") 
plt.show()

'''---------------------------------------------------------------------------------------------------------------------105'''
# Euler's formula. 

k = np.pi/6
m = 2.3

eul = m*np.exp(1j*k)
cis = m*(np.cos(k) + 1j*np.sin(k))
print(cis,"\n",eul)

mag = np.abs(eul)
ang = np.angle(eul)

plt.polar([0,ang], [0,mag], 'r')
plt.polar(k,m,'bo')

plt.show()

'''----------------------------------------------------------------------------------------------------------------------106'''
#Euler's formula: Exercise


def eulerFromCosSin():
    re = eval(input("Cosine part:"))
    im = eval(input("Sine part:"))
    
    m = np.sqrt(re**2  + im**2)
    k = np.arctan2(im,re)
    
    plt.polar([0,k], [0,m])
    plt.title("me$^{i\\phi}$, m=%g, $\\phi$ = %g" % (m,k))
    plt.thetagrids([0, 45, 130, 200, 222.2]) # esto es para controlar las diviciones de la cuadricula. Si dejamos la lista en blanco, la cuadricula no tendra puntos de referencia. 
    plt.show()


eulerFromCosSin()


'''--------------------------------------------------------------------------------------------------------------------107'''
# Exercise: Random explodimg Euler

nvecst = 200

m = np.random.rand(nvecst)
k = np.random.rand(nvecst)*2*np.pi

for i in range(0, nvecst):
    r = np.random.rand()
    
    if r < .4:
        colors = [1,.2,.7]
    elif r>.4 and r<.8:
        colors = [.7,.2,1]
    else:
        colors = [0,1,0]
    plt.polar([0,k[i]], [0,m[i]], color = colors)

plt.axis("off")
plt.show()

'''-=-------------------------------------------------------------------------------------------------------------------108'''
#Random snakes with cosine and sine. 
t = np.linspace(0,8*np.pi, 1000)


r1 = np.random.rand()
r2 = np.random.rand()

x = np.cos(r1*t)
y = np.sin(r2*t)

x = np.append(x,x[0])
y = np.append(y,y[0])

plt.plot(x,y)
plt.axis("square")
plt.axis([-1.1,1.1,-1.1,1.1])
plt.title("$r_1$=%s , $r_2$=%s" % (np.round(r1,2),round(r2,2)))
plt.show()


'''---------------------------------------------------------------------------------------------------------------------109'''
#Bud Hunt

s = np.random.randn(100,1)
# plt.imshow(s) # esto esta mal, porque se ve un poco feo. Mejor es con un plt.plot()
plt.plot(s,'s')
plt.show()

# --

mat = np.random.randint(3, 21, (30,20) )

plt.imshow(mat)
plt.colorbar()
plt.show()

#--
n = 100

randphases = np.random.randn(n)+2*np.pi  # Creo que podriamos usar ambos codigos aqui. 
randphases = np.random.randn(n)*2*np.pi

for i in range(0,n):
    plt.polar([0,randphases[i]],[0,1], '-o', color = np.random.rand(3), markersize = 20, alpha = .3)
    # plt.polar(randphases[i], 1, '-o', color = np.random.rand(3), markersize = 20, alpha = .3) Este no sirve

plt.show()

#--

n = 100
a = np.linspace(0,1,n)
p = np.linspace(0,4*np.pi, n)

plt.polar(p,a)
plt.show()

#--

n = 10 
rad = np.logspace(np.log10(.001), np.log10(2*np.pi), n)

print(np.rad2deg(rad))

#--

ang = np.logspace(np.log10(00.000001), np.log10(2*np.pi), 10)

print(ang)
np.cos(ang)**2 + np.sin(ang)**2 


#--

p = np.pi/4
m = .5

eulr = m*np.exp(p*1j)

mag = np.abs(eulr)
ang = np.angle(eulr)

plt.polar([0,ang], [0,mag], 'b', linewidth = 3)
plt.show()






