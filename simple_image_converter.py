# simple_image_converter.py
from PIL import Image

def convert_image(input_file, output_file, format):
    image = Image.open(input_file)
    image.save(output_file, format=format.upper())

if __name__ == "__main__":
    input_file = input("Enter the input image file: ")
    output_file = input("Enter the output image file: ")
    format = input("Enter the output format (e.g., PNG, JPEG): ")
    convert_image(input_file, output_file, format)
    print(f"Image saved as {output_file} in {format} format")
