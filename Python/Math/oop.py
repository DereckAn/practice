# from openpyxl import workbook
# from openpyxl import load_workbook


# hola = load_workbook("C:\\Users\\Pito de Abuelo\\Documents\\Archivos de excel\\MATRIZ ACTUALIZADA CORPACEROS 2022.xlsx")
# adios = load_workbook("C:\\Users\\Pito de Abuelo\\Documents\\Archivos de excel\\HISTORIA NUTRICIONAL ACTUALIZADA.xlsm")

# hhoja = hola['valoracion 2022']
# aadios = adios['Vacio']
# print((hhoja['C2']).value)
# print((aadios['P2']).value)

# aadios['P11'].value = (hhoja['C2']).value


'''---------------------------------------------------------------------------------------------------------------------------- __eq__ '''
# by default, intansces of the same class in python are not equal
# we customize object equality by defining __eq__

class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
        
    def __repr__(self): #Se supone que este metodo es para cambiar cono se representan los objetos en la pantalla. 
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    
    def __eq__(self,other):  # Este metodo es para hacer que dos objetos sean iguales para la computadore. 
        # return True Esto es para que todos los objetos sean igueales. 
        if not isinstance(other, Book):   # esto es para que sean del mnismo objeto. 
            return False
        return self.title == self.title and self.author == other.author  # Aqui estamos solo comparando dos parametros. 
    
    def __ne__(self, other): # este metodo es casi lo mismo que la funcion anterior solo que hace lo opuesto. 
        if not isinstance(other, Book):   # esto es para que sean del mnismo objeto. 
            return False
        return self.title != self.title and self.author != other.author
    
    def __hash__(self):
        return hash((self.title, self.author))
        

b = Book("Libro de dereck", " Dereck ", "Cientifico", 600)
b2 = Book("Libro de dereck", " Dereck ", "Cientifico", 600)

print(b==b2) #Esto es falso porque cada objeto ocupa un diferente espacio en la memoria 

print(id(b) ) # 2955095026288  Este es el espacio donde se encuentra
print(id(b2)) # 2955095018080


#-------
from collections import namedtuple  # esto es como hacer una clase pero de diferente manera.

essay = namedtuple("essay", ["title", "author"])
e = essay("Libro de dereck", " Dereck ")

print(e) #  essay(title='Libro de dereck', author=' Dereck ')

print(e==b) # Esto es false   PERO PERO PERO  sin no ponemos en isinstance en la funcion __eq__ la computadora podria tomarlo como verdadero. 


'''------------------------------------------------------------------------------------------------------------------------------- Hasting and mutability'''

l = ["dereck", 5]  # I cannot use hash with list, set, or dictionaries 

name_str = "Dereck"
num_int = 24
both_tuple = (name_str, num_int)

print(hash(name_str), hash(num_int), hash(both_tuple))

'''------------------------------------------------------------------------------------------------- Hashable book'''

# Podemos hacer hash a un instance de una clase  pero solo a las clases tienen sus reglas por default. 
# la calse que hemos creado no podemos hacerle hash porque modificamos las reglas utilizando __eq__ 
# Pero si ponemos __hash__(self): podemos volver a aherle hash a nuestra clase 

'''------------------------------------------------------------------------------------------------- Hashing gotcha'''

'''----------------------------------------------------------------------------------------------------- Exercise'''
class Contact:
    def __init__(self, name, last_name, age, phone=None, email=None, display_mode = "masked"):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
        
    def __repr__(self):
        if self.display_mode =="masked":
            return f"Contact(name= {self._obfuscate(self.name)}, last name= {self._obfuscate(self.last_name)})"
        return f"Contact(name= {self.name}, last name= {self.last_name}, age = {self.age}, phone = {self.phone}, email = {self.email})"
    
    def __str__(self):
        return f"{self.name[0]}{self.last_name[0]}"
    
    def __eq__(self,other):  # Este metodo es para hacer que dos objetos sean iguales para la computadore. 
        # return True Esto es para que todos los objetos sean igueales. 
        if not isinstance(other, Contact):   # esto es para que sean del mnismo objeto. 
            return False
        
        if (self.email is not None and self.email == other.email) or ( self.phone is not None and self.phone == other.phone):
            return True
        
        return self.name == other.name and self.last_name == other.last_name  # Aqui estamos solo comparando dos parametros. 
        
    def __hash__(self):
        return hash((self.name , self.last_name, self.phone, self.email))
    
    
    def __format__(self, __format_spec):
        if __format_spec != "masked":
            return f"Contact(name= {self.name}, last name= {self.last_name}, age = {self.age}, phone = {self.phone}, email = {self.email})"
        return repr(self)
    
    @staticmethod
    def _obfuscate(text):
        helf_leght = len(text) // 2 
        return text[:helf_leght] + "*" * (helf_leght + 1)
    
    def __gt__(self, other): # Este es otro metodo para comparar "greater than"
        if not isinstance(other, Contact):
            return NotImplemented
        return self.age > other.age
    
    def __bool__(self):  # Como yo lo entiendo es para mostrar si es verdadero o falso el instance de la clase.
        return bool(self.age) and not(self.age < 1)
    
    def __len__(self):  # Cuando esta este metodo definido (como ahorita) el metodo __bool__ tambien se ve afectado. 
        return self.age
        


d1 =  Contact("Dereck", "Angeles", 24 , 8014723664, "dereck angeles150718@gmail.com")

f"{d1:unmasked}"
print(d1)


from functools import total_ordering  # Esto es para reducir la menra en la que modificamos las clases. Se supone que vamos a resumir todos los metodos 
# Hay unas funciones donde algunos metodos son redundantes, This function supports the rest of the methods even if we do not implemented in the base clase. 


Contact = total_ordering(Contact)  # With this code we implement de function above   ------ This is one way 

@total_ordering  # This is another way to implement the code in our class 
class Story:
    def __init__(self, name, long, place, people):
        self.name = name
        self.long = long
        self.place = place
        self.people = people
    

# para customizar el valor buleano de una instance de una clase.  __bool__ 



 



'''-----------------------------------------------------------------------------Otra Manera de Crear Clases-----------------------------------------'''
from dataclasses import dataclass

@dataclass
class Hola:
    largo: int
    nombre: str
    color: str
    age: int
    sino: bool
    

d1 = Hola(5, "Dereck", "Azul", 24, True)

print(d1)
    
    











