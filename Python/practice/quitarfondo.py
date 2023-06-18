from rembg import remove
from PIL import Image
# import sys

def main1(input_path):
    
    input = remove(input_path) # Esto es por si quieres remover el fondo. 
    nombrefoto = "pato.ico"   # Este es el nombre de la foto que tendra. 
    input.save(f"/home/dereck/Downloads/{nombrefoto}") # esta es la direccion en la que se almacenara laa foto. 
    
input_path = Image.open("/home/dereck/Downloads/pato.jpg")  # Recuerda que cada imagen tiene una direccion diferente. Y no olvides el tipo de formato. 


main1(input_path)


# Este codigo solo srive para python entre 3.7 y 3.11

