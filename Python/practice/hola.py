hola = "hola dereck como estas"

# print(len(hola.split()))
hola2 = []
for i in range(len(hola.split())):

    print(i)
    if i == 0:
        print(hola.split()[0])
        hola2.append(hola.split()[0])
    else:
        print(hola.split()[i][::-1])
        hola2.append(hola.split()[i][::-1])
s = " ".join(hola2)

print(s)




def reverse_long_words(string):
    words = string.split()

    # Reverse long words and rebuild the string
    new_string = ' '.join([word[::-1] if len(word) >= 5 else word for word in words])

    return new_string

# --------------------------------------------------------------
def narcissistic( value ):
    value2 = list(str(value))
    digitos = [(int(value2))**(len(str(value))) for value2 in value2]
    print(sum(digitos))
    
    if sum(digitos) == value:
        return print(True)
    else:
        return print(False)
narcissistic(45)

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))



# -----------------------------------------------------------------------
def digital_root(n):
    suma = 0
    if len(str(n)) == 1:
        return print(n)
    else: 
        for i in str(n):
            suma += (int(i))
    return print(digital_root(suma))
        
digital_root(151)

# 3-----------------
def digital_root(n):
	return n%9 or n and 9 

print(digital_root(151))





# -----------------------------------
# from ast import List
from itertools import combinations

s, n = input().split()
s, n = sorted(s), int(n)
print(*(''.join(x) for k in range(n) for x in combinations(s, k + 1)), sep='\n')







class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lista2 = [x for x in nums ]
        print(lista2)


    twoSum([2,7,11,15], 9)

        

# -------------------------------------------------------------------------------------
import textwrap
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

def wrap(string, max_width):
    palabra = textwrap.TextWrapper(width=max_width)
    lista = palabra.wrap(text=string)
    print(lista)
    print(palabra)
    for i in lista:
        return i
wrap(string, max_width)



print(-221%23)
print(13%3)
print(-97%11)