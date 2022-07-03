'''
Tutorial on Kivy: https://realpython.com/mobile-app-kivy-python/
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer 
from kivy.uix.screenmanager import ScreenManager, Screen
from functions import *
from PIL import Image
from kivy.properties import StringProperty
import os
from os import startfile
from kivy.core.window import Window

media_type = ""
platform = ""
original_file_name = ""
compressed_filename = ""
error_message = ""

class HomeScreen(Screen):
    pass

class PlatformScreen(Screen):
    pass

class FileSelection(Screen):
    pass

class FileDownloadPicture(Screen):
    pass

class FileDownloadVideo(Screen):
    pass

class Error(Screen):
    def on_enter(self, *args):
        global error_message
        self.ids.errorMessage.text = error_message
        print(self.ids.errorMessage.text)

class WindowManager(ScreenManager):
    compressed_media = StringProperty('')
    result = StringProperty('')
    original_file = StringProperty('')

kv = Builder.load_file("interface.kv")

class MyMainApp(App):
    def build(self):
        return kv

    def on_press_homescreen_button(self, instance):
        global media_type
        media_type = instance.text

    def on_press_platform_button(self, instance):
        global platform
        platform = instance.text

    def selected(self, selectedfile):   
        global kv
        
        file_name = selectedfile[0]

        global original_file_name, compressed_filename, error_message
        original_file_name = file_name

        if media_type == "Compress Video":
            print("converting video")
        else:
            original_file = Image.open(file_name)
            print_file_info(original_file, file_name, "Original")

        compressed_file_name = get_compressed_file_name(file_name)
        
        if media_type == "Compress Video":
            result = compress_video_platform(platform, file_name, compressed_file_name)
        else:
            result = compress_picture_platform(platform, original_file, compressed_file_name, file_name)

        if not isinstance(result, str):
            compressed_filename = result[0]
            result = result[1]

        kv.compressed_media = self.getCompressedFile()
        kv.original_file = self.getOriginalFile()

        if result == "Success":
            print("Successfully compressed")
            if media_type == "Compress Video":
                pass #ToDo
            else:
                compressed = Image.open(compressed_filename)
                print_file_info(compressed, compressed_filename, "Compressed")
            return "Success"
        else:
            if result == "Unsuccess":
                error_message = "Media could not be compressed"
            elif result == "No need to compress":
                error_message = "Media already with less than file size limit"
            elif result == "Error":
                error_message = "Error"
            elif result == "Cancel":
                error_message = "Canceled by user"
            return "Error"

    def getCompressedFile(self):
        global compressed_filename
        return compressed_filename

    def getOriginalFile(self):
        global original_file_name
        return original_file_name

    def open_folder(self):
        folder = "./converted_media/"
        folder = os.path.realpath(folder)
        startfile(folder)
        
    def open_compressed_video(self):
        global compressed_filename
        startfile(os.path.normpath(compressed_filename))
    
    def open_original_video(self):
        global original_file_name
        startfile(original_file_name)
        
    def on_stop(self):
        Window.close()

        
if __name__ == "__main__":
    MyMainApp().run()

