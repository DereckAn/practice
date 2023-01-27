from rembg import remove
from PIL import Image
# import sys

def main1(input_path):
    
    input = remove(input_path) # Esto es por si quieres remover el fondo. 
    nombrefoto = "hola1.ico"   # Este es el nombre de la foto que tendra. 
    input.save(f"D:\Fotos\Videos descargados de youtube por python\{nombrefoto}") # esta es la direccion en la que se almacenara laa foto. 
    
input_path = Image.open("c:\Vs code\Proyectos\Python\practice\web.png")  # Recuerda que cada imagen tiene una direccion diferente. Y no olvides el tipo de formato. 


main1(input_path)




