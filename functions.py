import os
from hurry.filesize import size

'''
This function should receive a number from the frontend (once the user clicks on the platform icon)
and should proceed with the corresponding compression rate / quality
'''
def get_platform(user_selection):
    match user_selection:
        case 1:
            return "Facebook"
        case 2:
            return "Instagram"
        case 3:
            return "Twitter"
        case 4:
            return "LinkedIn"
        case 5:
            return "Discord"
        case 6:
            return "Messenger"
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
    compressed_optimized_file = "pictures/" + file_name + "_compressed_optimized." + file_extension

    return [compressed_file, compressed_optimized_file]   

'''
This function prints the file information: size in pixels and size in MB
'''
def print_file_info(file, file_path, display_text):
    print("Size of " + display_text + " picture: " + str(file.size[0]) + " X " + str(file.size[0]))
    print(display_text + " file size: " + str(size(os.path.getsize(file_path))) + " bytes")