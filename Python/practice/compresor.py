from PIL import Image
image = Image.open("C:\Users\Pito de Abuelo\Downloads\IMG_1506.jpg")

image = image.convert("RGB")

image.save("patotierno.jpg", quality=30)
