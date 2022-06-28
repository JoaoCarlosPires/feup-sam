'''
Tutorial on Kivy: https://realpython.com/mobile-app-kivy-python/

cross-platform Python framework
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from functions import *
from PIL import Image
from kivy.properties import StringProperty
from kivy.setupconfig import USE_SDL2

class HomeScreen(Screen):
    pass

class PlatformScreen(Screen):
    pass

class FileSelection(Screen):
    pass

class FileConversion(Screen):
    pass

class FileDownload(Screen):
    pass

class Error(Screen):
    pass

class WindowManager(ScreenManager):
    compressed_picture = StringProperty('sample_pictures/rome_17mb.jpg')
    result = StringProperty('test')
    errorMessage = StringProperty('test')
    original_file = StringProperty('sample_pictures/rome_17mb.jpg')

kv = Builder.load_file("interface.kv")

media_type = ""
platform = ""
original_file_name = ""
compressed_filename = ""
error_message = ""

class MyMainApp(App):
    att = ""

    def build(self):
        return kv

    def on_press_homescreen_button(self, instance):
        global media_type
        media_type = instance.text

    def on_press_platform_button(self, instance):
        global platform
        platform =  instance.text

    def selected(self, filename):
        file_name = filename[0]

        global original_file_name, compressed_filename, error_message
        original_file_name = file_name

        original_file = Image.open(file_name)
        print_file_info(original_file, file_name, "Original")
        compressed_file_name = get_compressed_file_name(file_name)
        result = compress_by_platform(platform, original_file, compressed_file_name, file_name)

        if len(result) > 1:
            compressed_filename = result[0]
            result = result[1]

        if result == "Success":
            print("Successfully compressed")
            compressed = Image.open(compressed_filename)
            print_file_info(compressed, compressed_filename, "Compressed")
            return "Success"
        else:
            match result:
                case "Unsuccess":
                    error_message = "Picture could not be compressed"
                case "No need to compress":
                    error_message = "Picture already with less than file size limit"
                case "Error":
                    error_message = "Error"
                case "Cancel":
                    error_message = "Canceled by user"
            return "Error"

    def getCompressedFile(self):
        global compressed_filename
        return compressed_filename

    def getOriginalFile(self):
        global original_file_name
        return original_file_name

    def getErrorMessage(self):
        global error_message
        return error_message

    def share(self, path):
        if platform == 'android':
            from pyjnius import cast
            from pyjnius import autoclass
            if USE_SDL2:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
            else:
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')
            Uri = autoclass('android.net.Uri')
            File = autoclass('java.io.File')

            shareIntent = Intent(Intent.ACTION_SEND)
            shareIntent.setType('"image/*"')
            imageFile = File(path)
            uri = Uri.fromFile(imageFile)
            parcelable = cast('android.os.Parcelable', uri)
            shareIntent.putExtra(Intent.EXTRA_STREAM, parcelable)

            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(shareIntent)

            print("Teste")
        print("Teste2")

        
if __name__ == "__main__":
    MyMainApp().run()

