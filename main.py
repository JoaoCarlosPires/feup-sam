'''
PILLOW (PIL) documentation: https://pillow.readthedocs.io/en/stable/
'''

from PIL import Image
import tkinter as tk
from tkinter import filedialog
from functions import *

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

foo = Image.open(file_path)
print_file_info(foo, file_path, "Original")

file_names = get_compressed_file_name(file_path)

foo.save(file_names[0],quality=95)
foo.save(file_names[1],optimize=True,quality=95)

compressed = Image.open(file_names[0])
compressed_optimized = Image.open(file_names[1])

print_file_info(compressed, file_path, "Compressed")
print_file_info(compressed_optimized, file_path, "Compressed and Optimized")
