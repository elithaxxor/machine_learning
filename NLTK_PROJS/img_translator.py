class ImageTranslate():
    import pprint
    from translate import Translator
    from googletrans import Translator
    import pytesseract, os, platform, subprocess, time, easyocr
    from subprocess import call
    from PIL import Image
    from IPython.display import display, Image
    
    def __init__(self):
        self.cwd = os.getcwd()
        super(ImageTranslate).__init__()
        print(f'[+] Enter Image Location and Image name in single str. [+]\n\t\t [+][{self.cwd}]\n[+]** ')
        self.img_loc = input('')
        self.cv2 = cv2
        self.pytesseract = pytesseract.tesseract_cmd()
        self.custom_config00 = r'--oem 3 --psm 6'
        self.pp = pprint.PrettyPrinter(indent=3)
        self.translator_img = Translator()
        self.latin_translator = Translator(to_lang="zh");
        self.spanish_translator = self.translator_img(to_lang="es")
        self.reader = easyocr.Reader(['en'])
        self.cv_img = cv2.imread(self.img_loc)
        self.cv_img = cv2.cvColor(self.cv_img, cv2.COLOR_BGR2RGB)
        self.data_read = self.reader.readtext(self.img_loc)
        print('dataread', self.data_read)
        self.translation = self.translator_img.detect(self.data_read)
        print('translation', self.translation)
        ## reading text using text blob
        self.blobber = TextBlob(self.reader)
        print()
        print(self.blobber)
        print()
        self.blobber = TextBlob(self.data_read)

    def __enter__(self):
        print('enter method called'); return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called'); print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')

    def __repr__(self):
        return f"\n <From __REPR__  [self]: {self},[translator]: {self.translator} \n "

    def __str__(self):
        return f"\n <From __STR__  [self]: {self},[translator]: {self.translator}"

    def display_Originals(self):  ### Display images
        try:
            display(Image.open(self.img_loc))
            if display:
                print(f'[+] Display Opened at [{time.ctime()}]')
            else:
                print(f'[-] Viewer Could not Open Picture ')
                pass
            cv2.imshow(self.img_loc)
            if cv2.imshow:
                print(f'[+] CV2 display opened [+]')
                cv2.waitKey()
                key = cv2.waitKey(0) & 0xFF  # 1 ms delay
                if key == ord('q'):
                    print(f'{red} [-] ** User Quit Key Hammered ** [-]')
            else:
                print(f'{red}[-] Viewer Could not Open Picture {reset}')
        except Exception as e:
            print(e)


    class image_foreplay():
        def __init__(self):
            self.cv_image = self.cv_img

        def __enter__(self):
            print('[SYSTEM] SCRIPT INITATED ENTER METHOD '); return self

        def __exit__(self, exc_type, exc_value, exc_traceback):
            print('[SYSTEM]**Exit-Method Called'); print(
                f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')

        def greyScale(self):  ### Display images
            ## convert to grey scale
            greyScale = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Grey Scale', greyScale)
            cv2.waitKey(5000)
            custom_config = r'--oem 3 --psm 6 outputbase digits'

            Grey_cv2_dimen = pytesseract.image_to_string(greyScale, config=custom_config)  ## detecting height and width
            width, height = greyScale.shape
            print(f'[+] [GREYSCALE] :: Dimenensions --> {width} x {height}')
            greyScale_boxes = pytesseract.image_to_string(greyScale)
            return greyScale_boxes, Grey_cv2_dimen, width, height

        def blur(self):
            blur = cv2.GaussianBlur(self.cv2_img, (7, 7), cv2.BORDER_DEFAULT)

            self.cv2.imshow('blur', self.cv2_img)
            cv2.waitKey(5000)
            if cv2.waitKey(5000) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

        def cascade(self):
            cascade = cv2.Canny(self.cv2_img, 125, 175)
            cv2.imshow('cascade', cascade)
            cv2.waitKey(5000)

            if cv2.waitKey(5000) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

        def dialated(self):
            dilated = cv2.dilate(dilated, (3, 3), iterations=1)

            cv2.imshow('dilated', dilated)
            cv2.waitKey(5000)
            if cv2.waitKey(5000) & 0xFF == ord('q'): cv2.destroyAllWindows()


#  print(f'[+] Detected Language [GOOGLE] {self.translator.detect(self.inQuestion)}') print(f'[+] Translated Text BLOBBER] .. '#print(f"[+] Translated Text [GOOGLE]: \n [{self.translator.translate(self.inQuestion, dest='en')}")
def text_from_img(self, data):
    try:
        print('\n', 'X' * 50)
        print(f'[+] Translating :: [WILDCARD] \n [{self.inQuestion=}]')
        print(
            f'[+] Decoding [{self.data_read}].. ')
        print(f'[+] CV2 read_data {"X" * 50} \n\n[{self.cvImg_data}]')
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        print(f'[+] CV2 read_data [WITH CUSTOM CONFIG PARAM ]{"X" * 50} \n\n[{self.cvImg_data}]')
        print('[+] Reading Data using Blobber')
        print(f'[+]data_read {self.data_read}')  # reader
        print(f'blobber{self.blobber}')
        print(f'cv2 {self.cv2_data}')
        pprint.pprint(self.cvImg_data)
        print(
            f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t{yellow} {bblue} ---> {self.blobber.translate(to="fr")}].. {reset} <-- {reset}')
        print(f'[+] Detected Language [BLOBBER] {self.lang01}].. ')

        print('X' * 50, '\n')
        self.pp.pprint([text[-2] for text in self.data_read])
        print('\n', 'X' * 50)
        print('[+] Reparsing, just incase non-english verbagh [+] ')
        print(self.translation)

    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
    pass


def img_draw(self, type, _boxes, _dimen, _width, _height):
    print(f'[+] Drawing [{type}] \n[{time.ctime()}]')
    _boxes_len = len(_boxes)
    _dimen_len = len(_dimen)
    print(f'[{_width}x{_height} --> [{_dimen}]]')
    for gb in _boxes.splitlines():
        print(f'[+]--{gb}')
        gbSplit = gb.split(''); print(gbSplit)  ## creates list for easier element access
    if _boxes_len == _dimen_len:
        print(f"{yellow} [+] Succesfully parsed through boxes:: \n\t\t**[FILE] [{file}]\n\t\t {time.ctime()}")
    if cv2.waitKey(5000) & 0xFF == ord('q'): cv2.destroyAllWindows()


def translate_to_spanish(self):
    try:
        print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion=}]')
        self.spanish_translator = Translator(to_lang="es")
        print(f'[+] Translating :: \m [{self.data_read}]')
        print(self.spanish_translator.translate(self.data_read))

    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
        pass



def translate_to_latin(self):
    try:
        self.spanish_translator = Translator(to_lang="es")
        print(f'[+] Translating :: \m [{self.data_read}]')
        print(self.spanish_translator.translate(str(self.data_read)))
    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
        pass


def translate_to_spanish0(self):
    try:
        print('\n', 'X' * 50)
        print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion=}]')
        print(f'[+]-[SPANISH]-[+] Translated Text [+]-[BLOBBER]-[+] {self.blobber.translate(to="es")}].. ')
        print('X' * 50, '\n')

    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
        pass


def translate_to_french(self):
    try:
        print('\n', 'X' * 50)
        print(f'[+] ::  Translating :: [FRENCH]\n\t\t **[{self.inQuestion}]')
        print(f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+] {str(self.blobber.translate(to="fr"))}].. ')
        # print(f"[+]-[FRENCH]-[+] Translated Text [+]-[GOOGLE]-[+] [{self.translator.translate(self.inQuestion, dest='fr')}")
        print('X' * 50, '\n')
    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
        pass


def translate_to_latin0(self):
    try:
        print('\n', 'X' * 50)
        print(f'[+] ::  Translating :: [GOOGLE]\n\t\t **[{self.inQuestion=}]')
        print(f'[+]-[LATIN]-[+] Translated Text [+]-[BLOBBER]-[+] {self.blobber.translate(to="la")}].. ')
        # print(f"[+]-[LATIN]-[+] Translated Text [+]-[GOOGLE]-[+] [{self.translator.translate(self.inQuestion, dest='la')}")
        print('X' * 50, '\n')
    except AttributeError:
        print(f'{red} ill fix you later--google{reset}')
        pass
    except Exception as e:
        traceback.print_exc()
        print(f"{str(e)}")
        pass


if __name__ == '__main__':
    img_parser = ImageTranslate()
