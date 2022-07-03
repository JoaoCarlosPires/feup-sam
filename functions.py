'''
PILLOW (PIL) documentation: https://pillow.readthedocs.io/en/stable/
'''

import os
from hurry.filesize import size
from PIL import Image
import ffmpeg
import shutil

'''
This function should receive a number from the frontend (once the user clicks on the platform icon)
and should proceed with the corresponding compression rate / quality
'''
def compress_picture_platform(user_selection, image, file_name, original_file_name):
    if user_selection == "Facebook": 
        valid_types = ["JPEG", "JPG", "PNG", "BMP", "GIF", "TIFF"]
        return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
    elif user_selection == "Ig": #Instagram
        valid_types = ["JPEG", "JPG", "PNG", "BMP"]
        return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
    elif user_selection == "Twitter":
        valid_types = ["JPEG", "JPG", "PNG", "GIF"]
        return verify_compress(image, valid_types, file_name, original_file_name, 5000000, 1)
    elif user_selection == "LinkedIn":
        valid_types = ["JPEG", "JPG", "PNG", "GIF"]
        return verify_compress(image, valid_types, file_name, original_file_name, 5000000)
    elif user_selection == "Discord":
        valid_types = ["JPEG", "JPG", "PNG", "GIF"]
        return verify_compress(image, valid_types, file_name, original_file_name, 8000000)
    elif user_selection == "Messenger":
        valid_types = ["JPEG", "JPG", "PNG", "GIF"]
        return verify_compress(image, valid_types, file_name, original_file_name, 25000000)
    else:
        return "Error"

def compress_video_platform(user_selection, original_file_name, file_name):
    if user_selection == "Facebook": 
        return verify_video(file_name, original_file_name, 10000000)
    elif user_selection == "Ig": #Instagram
        return verify_video(file_name, original_file_name, 100000)
    elif user_selection == "Twitter":
        return verify_video(file_name, original_file_name, 512000)
    elif user_selection == "LinkedIn":
        return verify_video(file_name, original_file_name, 5000000)
    elif user_selection == "Discord":
        return verify_video(file_name, original_file_name, 8000)
    elif user_selection == "Messenger":
        return verify_video(file_name, original_file_name, 25000)
    else:
        return "Error"

def verify_video(file_name, original_file_name, final_size):
    extension = (file_name.split(".")[-1]).upper()
    if extension != "MP4":
        file_name = file_name.split(".")[0] + ".mp4"
    file_stats = os.stat(original_file_name)
    if file_stats.st_size <= final_size:
        return "No need to compress"
    return [file_name, compress_video(original_file_name, file_name, final_size)]
    

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

'''
This function takes a video file(mp4 or mov) and compresses it to the target_size defined (target_size is in kb)
if target_size = 0, function determines ideal min size. output_file_name requires an extension
If video bit rate < 1000, it will throw exception Bitrate is extremely low
'''
def compress_video(video_full_path, output_file_name, target_size):
    output_file_name = os.path.normpath(output_file_name)
    output_file_name = output_file_name.split(os.sep)
    
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    filename,file_extension = os.path.splitext(video_full_path)
    #print("file extension: " , file_extension)
    file_extension = file_extension.replace('.','')

    min_audio_bitrate = 32000
    max_audio_bitrate = 256000
    
    probe = ffmpeg.probe(video_full_path)
    
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    try:
        audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    except:
        print("NO AUDIO MOTHERFUCKER")
        no_audio = 1
        audio_bitrate = 0
        

    # Target total bitrate, in bps.
    if target_size == 0:
        target_size = get_best_min_size(video_full_path)
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if(not no_audio):
        if 10 * audio_bitrate > target_total_bitrate:
            audio_bitrate = target_total_bitrate / 10
            if audio_bitrate < min_audio_bitrate < target_total_bitrate:
                audio_bitrate = min_audio_bitrate
            elif audio_bitrate > max_audio_bitrate:
                audio_bitrate = max_audio_bitrate
    
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': file_extension}).overwrite_output().run()
    ffmpeg.output(i, output_file_name[1],**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}).overwrite_output().run()
    shutil.move(output_file_name[1],os.path.join(output_file_name[0],output_file_name[1]))
    return "Success"

'''
This function returns the ideal min size of a video in kB
'''
def get_best_min_size(video_full_path):
    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    ideal_size = (32000 + 100000) * (1.073741824 * duration) / (8 * 1024)
    print("Ideal size (kb): " + str(ideal_size))
    return ideal_size
