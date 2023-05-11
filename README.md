# ctaMTX

A Python library to write and read MTX files (Mediocre's Granny Smith File Format).

# Example usage

from ctamtx import write_mtx_file, read_mtx_file

input_file_path = "!!input.jpg"

output_file_path = "output.mtx"

write_mtx_file(input_file_path, output_file_path)

image = read_mtx_file(output_file_path)

if image:

    image.show()

