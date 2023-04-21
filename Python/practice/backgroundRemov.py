from backgroundremover import BackgroundRemover

# Set the input and output file paths
input_path = "/home/dereck/Downloads/pato.jpg"
output_path = "pato.png"

# Remove the background from the image
BackgroundRemover.remove(input_path, output_path)