import os, platform, subprocess, time, traceback
from translate import Translator
from subprocess import call
from textblob import TextBlob
import requests
import nlpcloud


import inspect
from PIL import Image
from IPython.display import display, Image
# from googletrans import Translator
import pprint  # googletrans


# pytesseract
# cv2
# easyocr

def animate_Rocket():
    distanceFromTop = 20
    while True:
        print("\n" * distanceFromTop)
        print("          /\        ")
        print("          ||        ")
        print("          ||        ")
        print("         /||\        ")
        time.sleep(0.2)
        os.system('clear')
        distanceFromTop -= 1
        if distanceFromTop == 15:
            break
            # distanceFromTop = 20

# translator = Translator(service_urls=[
#     'translate.google.com',
#     'translate.google.co.kr',
# ])
# Translator = translator.detect('hello assholes')
# print(Tranlsator)
# self.translator.detect(self.inQuestion)
# self.inQuestion = inQuestion
# self.translator = Translator
#  self.spanish_translator = translator.Translator(self.inQuestion)
class TextTranslate():
    def __init__(self):
        super(TextTranslate).__init__()
        print(f'[+]-[+] Img-Txt Translator [+]-[+]')
        print(f'[+] Input the text for translatin : \n[*]** ')
        self.inQuestion = input('')
        self.blobber = TextBlob(self.inQuestion)
        self.Translator = Translator()
        self.url = "https://nlp-translation.p.rapidapi.com/v1/translate"
        self.querystring = {"text": self.inQuestion, "to": "es", "from": "en"}
        self.headers = {
            'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
            'x-rapidapi-key': "b3fc8c54beeb2d6a128a7eb10a461cbd36f4485e"
        }

        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        print(response.text)

        # self.blobber.detect_language()
        # self.lang01 = self.blobber.detect_language(self.inQuestion)
        self.translation = self.Translator.detect(self.inQuestion)
        print(self.translation)
        time.sleep(1.5)

    def __repr__(self):
        return f"\n <From __REPR__  [self]: {self},[translator]:"  # {self.translator} \n

    def __str__(self):
        return f"\n <From __STR__  [self]: {self},[translator]:"  # {self.translator}

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]');
        pass

    def translate_text(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] Translating :: [WILDCARD] \n \n\t\t --->[{self.inQuestion=}]');
            print(
                f'[+] {bblue} Decoding [{self.inQuestion}].. ')
            print(f'[+] Detected Language [BLOBBER]\n\t\t ---> {self.lang01}].. {reset}')
            print(
                f"[+] Translated Text [GOOGLE]: \n \n\t\t {yellow} --->[{Translator.translate(self.inQuestion.text, dest='en')} <--{reset}")
            print('X' * 50, '\n')

            time.sleep(2)

        except Exception as e:
            print(f"{str(e)} {traceback.print_exc()}")
        pass

    # print(f"[+] Detected Language [GOOGLE] \n\t\t --->{self.translator.detect(self.inQuestion, dest='en')}") # print(f'[+] Translated Text [BLOBBER] {self.blobber.translate(to="en")}].. ')
    def translate_to_spanish(self):
        try:
            print('\n', 'X' * 50);
            print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion}]{reset}')
            print(
                f'{bblue}[+]-[SPANISH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t {reset}{yellow} ---> {self.blobber.translate(to="es")}] <--{reset} ');
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google{reset}');
            pass
        except Exception as e:
            print('{str(e)} -->\n\t\t traceback.print_exc()');
            pass

    def translate_to_french(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] ::  Translating :: [FRENCH]\n\t\t **[{self.inQuestion=}]')
            print(
                f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t{yellow} {bblue} ---> {self.blobber.translate(to="fr")}].. {reset} <-- {reset}')
            # print(f"[+]-[FRENCH]-[+] Translated Text [+]-[GOOGLE]-[+]\n\t\t ---> [{self.translator.translate(self.inQuestion, dest='fr')}")
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google');
            pass
        except Exception as e:
            print(f"{str(e)} {traceback.print_exc()}{reset}")
        pass

    def translate_to_latin(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] ::  Translating :: [GOOGLE]\n\t\t **[{self.inQuestion}]')
            print(
                f'[+]-[LATIN]-[+] Translated Text [+]-[BLOBBER]-[+] {yellow}\n\t\t ---> {self.blobber.translate(to="la")}].. {reset}')
            # print(f"[+]-[LATIN]-[+] Translated Text [+]-[GOOGLE]-[+]\n\t\t ---> [{self.translator.translate(self.inQuestion, dest='la')}")
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google{reset}')
            pass
        except Exception as e:
            print(f"{str(e)}, traceback.print_exc()")
            pass


class Colors:
    reset = "\033[0m"
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"  # Black
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"  # Red
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"  # Green
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"

def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    for z, x in enumerate(period):
        print(x), time.sleep(.2)
        if z <= period_len:
            z += 1;
            print(f"{yellow}{x * z}{reset}");
            continue
        elif z == period_len:
            break
            
def clear(): os_name = platform.system(); _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')
  

############
# ---------#
###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


def main():
    TextTranslate()


if __name__ == '__main__':
    animate_Rocket()
    main()
