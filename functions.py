import os
from hurry.filesize import size
from PIL import Image

'''
This function should receive a number from the frontend (once the user clicks on the platform icon)
and should proceed with the corresponding compression rate / quality
'''
def get_platform(user_selection, image, file_name):
    match user_selection:
        case 1: #Facebook
            return compress_image(image, file_name, 8000000)
        case 2: #Instagram
            return compress_image(image, file_name, 8000000)
        case 3: #Twitter
            return compress_image(image, file_name, 5000000)
            # ToDo: .GIF -> 15MB instead of 5MB
        case 4: #LinkedIn
            return compress_image(image, file_name, 5000000)
        case 5: #Discord
            return compress_image(image, file_name, 8000000)
        case 6: #Messenger
            return compress_image(image, file_name, 25000000)
        case _:
            return "Error"

'''
This function returns the compressed and compressed & optimized file names
'''
def get_compressed_file_name(file_path):
    complete_path = file_path.split("/")
    file_name = complete_path[-1].split(".")[0]
    file_extension = complete_path[-1].split(".")[1]

    compressed_file = "pictures/" + file_name + "_compressed." + file_extension

    return compressed_file 

'''
This function prints the file information: size in pixels and size in MB
'''
def print_file_info(file, file_path, display_text):
    print("Size of " + display_text + " picture: " + str(file.size[0]) + " X " + str(file.size[0]))
    print(display_text + " file size: " + str(size(os.path.getsize(file_path))) + " bytes")

'''
This function compresses an image until it reaches the desired final_size.
If the image size is already bellow the final_size, it's not compressed.
The compression is limited until a quality of 50% (successfull in most of the cases).
'''
def compress_image(image, file_path, final_size):
    image.save(file_path,optimize=True,quality=100)
    if len(Image.open(file_path).fp.read()) <= final_size:
        return "No need to compress"
    for i in range(95, 50, -5):
        image.save(file_path,optimize=True,quality=i)
        if len(Image.open(file_path).fp.read()) <= final_size:
            return "Success"
    return "Unsuccess"

'''
This function checks if the file extension is in the list of valid types.
If it isn't, then prompts the user to select the new format or to cancel.
'''
def check_image_type(file_name, valid_types):
    return "ToDo"    
    