import os
import struct
from PIL import Image

def write_mtx_file(input_file_path, output_file_path):
    try:
        # Check if input file exists
        if not os.path.exists(input_file_path):
            print("Input file does not exist. Program terminated.")
            return

        # Read JFIF header and write it to the output stream
        with open(input_file_path, 'rb') as input_file:
            with open(output_file_path, 'wb') as output_file:
                header = input_file.read(18)
                output_file.write(header)

                # Read image data from separate input stream and write it to the output stream in MTX format
                image = Image.open(input_file_path)
                width, height = image.size
                output_file.write(struct.pack('>i', width))
                output_file.write(struct.pack('>i', height))

                for y in range(height):
                    for x in range(width):
                        red, green, blue = image.getpixel((x, y))
                        output_file.write(struct.pack('BBB', red, green, blue))

    except IOError as e:
        print("An error occurred: ", e)

def read_mtx_file(input_file_path):
    try:
        with open(input_file_path, 'rb') as input_file:
            # Skip the JFIF header
            input_file.read(18)

            # Read width and height
            width = struct.unpack('>i', input_file.read(4))[0]
            height = struct.unpack('>i', input_file.read(4))[0]

            # Create a new PIL image
            image = Image.new('RGB', (width, height))

            for y in range(height):
                for x in range(width):
                    red, green, blue = struct.unpack('BBB', input_file.read(3))
                    image.putpixel((x, y), (red, green, blue))

        return image

    except IOError as e:
        print("An error occurred: ", e)
        return None
