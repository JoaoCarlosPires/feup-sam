'''
PILLOW (PIL) documentation: https://pillow.readthedocs.io/en/stable/
'''

from distutils.log import error
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from functions import *

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

foo = Image.open(file_path)
print_file_info(foo, file_path, "Original")

file_name = get_compressed_file_name(file_path)

user_selection = input("Please select one platform:\n\n1.Facebook\n2.Instagram\n3.Twitter\n4.Linkedin\n5.Discord\n6.Messenger\n\nYour selection: ")

result = get_platform(int(user_selection), foo, file_name)

match result:
    case "Success":
        print("Successfully compressed")
        compressed = Image.open(file_name)
        print_file_info(compressed, file_name, "Compressed")
    case "Unsuccess":
        error("Picture could not be compressed")
    case "No need to compress":
        print("Picture already with less than file size limit")
    case "Error":
        error("Error")
    case "Cancel":
        print("Canceled by user")
    case _:
        error("Default error")