import sys

from numpy import append
sys.setrecursionlimit(1000)  # This is to set another limit when we use recurcion. To avoid a bucle. 

'''--------------------------------------------- Recursion in 3 steps -----------------------------------------------------'''
def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a whole positive number"
    print(n)
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


def factorialdos(n):
    assert n >= 0 and int(n) == n, "The number must be a whole positive number"
    print(n)
    if n in [0,1]:
        return 1
    else:
        return n * factorialdos(n-1)
        
print(factorialdos(5))

'''--------------------------------------------------- Fibonacci ----------------------------------------------------------'''

def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be a whole positive number"
    if n in [0,1]:
        return n
    else:    
        return  fibonacci(n-1) + fibonacci(n-2)
 
print(fibonacci(3))


'''----------------------------------------------------  Power  ------------------------------------------------------------------'''

def power(num, pow):
    if pow == 0:
        return 1
    elif pow < 0:
        return 1/ (num * power(num, pow+1))  # Aqui cambiamos la resta por una suma para que se hacerque al 0 
    return num * power(num, pow-1)  # ponemos la resta para que se acerque al cero. 

print(power(2,-1))

'''------------------------------------------------------ GCD ----------------------------------------------------------------'''
 # tenemos que usar el algoritmo de euclides. 
def gcd(a,b):
    assert int(a) == a and int(b) == b, "The numbers must be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(48,18))

'''-------------------------------------------- decimal to binary ------------------------------------------------------------'''

def convertion(a):
    if a == 0 :
        return 0;
    return a%2 + 10 * convertion(int(a/2))



print(convertion(10))



'''------------------------------------------SomeRecursive ------------------------------------------------------------'''


def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

someRecursive([1,2,3,4], isOdd) # true
someRecursive([4,6,8,9], isOdd) # true
someRecursive([4,6,8], isOdd) # false









