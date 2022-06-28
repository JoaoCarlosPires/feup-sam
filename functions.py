'''
PILLOW (PIL) documentation: https://pillow.readthedocs.io/en/stable/
'''

import os
from hurry.filesize import size
from PIL import Image

'''
This function should receive a number from the frontend (once the user clicks on the platform icon)
and should proceed with the corresponding compression rate / quality
'''
def compress_by_platform(user_selection, image, file_name, original_file_name):
    match user_selection:
        case "Facebook": 
            valid_types = ["JPEG", "JPG", "BMP", "GIF", "TIFF"]
            return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
        case "Instagram":
            valid_types = ["JPEG", "JPG", "PNG", "BMP"]
            return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
        case "Twitter":
            valid_types = ["JPEG", "JPG", "PNG", "GIF"]
            return verify_compress(image, valid_types, file_name, original_file_name, 5000000, 1)
        case "LinkedIn":
            valid_types = ["JPEG", "JPG", "PNG", "GIF"]
            return verify_compress(image, valid_types, file_name, original_file_name, 5000000)
        case "Discord":
            valid_types = ["JPEG", "JPG", "PNG", "GIF"]
            return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
        case "Messenger":
            valid_types = ["JPEG", "JPG", "PNG", "GIF"]
            return verify_compress(image, valid_types, file_name, original_file_name, 25000000)
        case _:
            return "Error"

'''

'''
def verify_compress(image, valid_types, file_name, original_file_name, final_size, twitter=0):
    if check_image_type(file_name, valid_types) != "Valid":
        new_extension = change_image_type(valid_types)
        if new_extension == "Error":
            return "Error"
        elif new_extension == "Cancel":
            return new_extension
        else:
            file_name = file_name.split(".")[0] + "." + new_extension
    
    if check_need_to_compress(original_file_name, final_size):    
        if "GIF" in file_name.upper() and twitter:
            return [file_name, compress_image(image, file_name, 15000000)]
        else:
            return [file_name, compress_image(image, file_name, final_size)]
    else:
        return "No need to compress"

'''
This function returns the compressed and compressed & optimized file names
'''
def get_compressed_file_name(file_path):
    if "/" in file_path:
        complete_path = file_path.split("/")
    else:
        complete_path = file_path.split("\\")
    file_name = complete_path[-1].split(".")[0]
    file_extension = complete_path[-1].split(".")[1]

    compressed_file = "converted_media/" + file_name + "_compressed." + file_extension

    return compressed_file 

'''
This function prints the file information: size in pixels and size in MB
'''
def print_file_info(file, file_path, display_text):
    print("Size of " + display_text + " picture: " + str(file.size[0]) + " X " + str(file.size[1]))
    print(display_text + " file size: " + str(size(os.path.getsize(file_path))) + " bytes")

'''
This function compresses an image until it reaches the desired final_size.
The compression is limited until a quality of 50% (successfull in most of the cases).
'''
def compress_image(image, file_path, final_size):
    for i in range(95, 50, -5):
        image.save(file_path,optimize=True,quality=i)
        if len(Image.open(file_path).fp.read()) <= final_size:
            return "Success"
    return "Unsuccess"

'''
If the image size is already bellow the final_size, it's not compressed.
'''
def check_need_to_compress(file_path, final_size):
    if len(Image.open(file_path).fp.read()) <= final_size:
        return 0 #No need to compress
    return 1

'''
This function checks if the file extension is in the list of valid types.
'''
def check_image_type(file_name, valid_types):
    extension = (file_name.split(".")[-1]).upper()
    for type in valid_types:
        if type == extension:
            return "Valid"
    return extension

def change_image_type(valid_types):
    '''
    print("The extension of the uploaded file is not valid in this platform. Do you want to convert it?\n")
    i = 1
    for type in valid_types:
        print(str(i) + ". " + type + "\n")
        i+=1
    print(str(i) + ". Do not convert\n")
    user_selection = int(input("Please select one option"))
    if user_selection > len(valid_types) + 1 or user_selection <= 0 :
        return "Error"
    elif user_selection == len(valid_types) + 1:
        return "Cancel"
    else:
        return valid_types[user_selection-1]
    '''
    return "JPG"