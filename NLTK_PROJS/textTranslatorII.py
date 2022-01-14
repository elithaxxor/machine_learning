import pprint
from translate import Translator
from googletrans import Translator
import pytesseract, os, platform, subprocess, time, easyocr
from subprocess import call
from PIL import Image
from IPython.display import display, Image



class TextTranslate():
    print(f'[+]-[+] Img-Txt Translator [+]-[+]')
    def __init__(self, toTranslate):
        super(TextTranslate).__init__()
        self.translator = Translator()
        self.translator.detect(toTranslate)
    def __repr__(self):
        return "<From __REPR__ [self]:%s [translator]:%s  >" % (self),(self.translator)
    def __str__(self):
        return "<From __STR__  [self]:%s [translator]:%s  >" % (self),(self.translator)

    def trans(self, sent):
        try:
            ans = self.translator.translate(sent)
            return ans
        except AttributeError:
            return 'Can\'t translate !'

print(f'[+] Input the text for translatin : \n[*]** ' )
inQuestion = input('')
with TextTranslate:
    ret = TextTranslate(inQuestion)
    print(f'[+] Translated Text')


class ImageTranslate():
    def __init__(self, toTranslate):
        super(ImageTranslate).__init__()
        self.pp = pprint.PrettyPrinter(indent=3)
        self.translator_img = Translator  ## backup translator
       # self.latin_translator = Translator(to_lang="zh")
        self.spanish_translator = Translator(to_lang="es")

        self.cwd = os.getcwd()
        self.reader = easyocr.Reader(['en']) # ocr reader
        print(f'[+] Enter Image Location and Image name in single str. [+]\n\t\t [+][{self.cwd}]\n[+]** ')
        self.img_loc = input('')
        self.data_read = self.reader.readtext(self.img_loc) ## read data info
        self.translation = self.translator_img.detect(self.data_read) ## may need to chanage to self.img_loc ?

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')

    def display_img(self): ### Display images
        display(Image.open(self.img_loc))
        if display:
            time00=time.time(); ctime00=time.ctime(time00)
            return f'[+] Display Opened at [{ctime00}]'
        else: return f'[-] Viewer Could not Open Picture'

    def text_from_img(self):
        self.pp.pprint([text[-2] for text in self.data_read])
        print('\n', 'X'* 50)
        print('[+] Reparsing, just incase non-english verbagh [+] ')
        print(self.translation)

    def translate_to_spanish(self):
        self.spanish_translator = Translator(to_lang="es")
        print(f'[+] Translating :: \m [{self.data_read}]')
        print(self.spanish_translator.translate(self.data_read))



print(f'[+] Quick Auto Translator [TEXT/IMG]' )
print('[+] The Img-Text translator will first attempt to translate just english, then reparse for non [en] lang. ')


with ImageTranslate as parseIMG:
    parseIMG. display_img()
