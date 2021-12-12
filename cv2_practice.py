import cv2

def image_parser(loc):
    cv2.namedWindow("Image")
    img = cv2.imread(str(loc))
    cv2.imshow('/shot', img)
    cv2.waitKey(5000)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return loc, img
    cv2.destroyAllWindows()
    return loc, img

### add _large behind .png to make larger
def expand_image(img):
    cv2.namedWindow("Image2")
    img_large = cv2.imread(img)
    cv2.imshow('/shot', img_large)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def display_video(vid):
    global capture
    capture = cv2.VideoCapture(vid)
    tf = capture.isOpened()
    if tf == False: capture.open(vid)
    while True:
        isTrue, frame = capture.read()
        print(f'[+] frame True? [{isTrue}] :: [{tf}]')
        cv2.imshow('video', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'): return frame
        capture.release()
        cv2.destroyAllWindows()
        return frame, capture

def live_capture():
    global capture
    capture = cv2.VideoCapture(0)
    tf = capture.isOpened()
    #if tf == False: capture.open()
    while True:
        isTrue, frame = capture.read()
        print(f'[+] frame True? [{isTrue}] :: [{tf}]')
        cv2.imshow('video', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'): return frame
        capture.release()
        cv2.destroyAllWindows()
        return frame, capture


## works best for existing video / streams
# also works for videos, images and webcam
def rescaleFrames(frame, scale=1.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height) # set tuple for return
    print(f'[+] Dimensions :: [{width}] x [{height}] :: [+]')
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

## only works for webcam
def rescaleRes(frame, scale=1.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    capture.set(3, width)  ## key 3 represients teh width
    capture.set(4, height) ## key 4 represents height


## live capture
vid, feed = live_capture()
rescale_feed = rescaleRes(vid)

## image parser and resizing
img_loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/shot.png"
loc, frame = image_parser(img_loc)
resize_image = rescaleFrames(frame)
resized_image = image_parser(img_loc) ## make it into a class for inhertiane. functionality is a pain the the ass

## video parser and resizing
vid_loc = "/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/random.mp4"
orig_vid, cap = display_video(vid_loc)
resize_vid = rescaleFrames(orig_vid)
rescale_res = rescaleRes(orig_vid)
resized_video = display_video(vid_loc)


import cv2
import numpy as np

loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/shot.png"
cv2.namedWindow("Image")
img = cv2.imread(str(loc))
cv2.imshow('/shot', img)
cv2.waitKey(5000)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

blank_image = np.zeros((500, 500, 3), dtype='uint8')
cv2.namedWindow("Blank Image")
cv2.imshow('blanl', blank_image)
cv2.waitKey(5000)
if cv2.waitKey(5000) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


def colorBg():
    ## full red
    blank_image[:] = 0, 0, 255
    cv2.imshow('full-red', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


## double
def drawLines():
    blank_image[200:300, 300:400] = 0, 0, 255
    cv2.imshow('double-color', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## rectangle inside box
    cv2.rectangle(blank_image, (0, 0), (250, 250), (0, 255, 0), thickness=2)
    cv2.imshow('Rectangle', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## circle
    cv2.circle(blank_image, (blank_image.shape[1] // 2, blank_image.shape[0] // 2), 40, (0, 255, 0), thickness=4)
    cv2.imshow('circle', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    # draw line
    cv2.line(blank_image, (0, 0), (blank_image.shape[1] // 2, blank_image.shape[0] // 2), (255, 255, 255))
    cv2.imshow('line', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


##1.5 = scale || (0,255,0) = color
def writeText():
    cv2.putText(blank_image, '[hello world]', (255, 255), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), thickness=3)
    cv2.imshow('TEXT', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def picPretty():
    ## convert to grey scale
    greyScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grey Scale', greyScale)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## blur
    blur = cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
    cv2.imshow('blur', blur)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## edge cascade:
    cascade = cv2.Canny(blur, 125, 175)
    cv2.imshow('cascade', cascade)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## dialated image
    dilated = cv2.dilate(cascade, (3, 3), iterations=1)
    cv2.imshow('dilated', dilated)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


## cv2.INTER_AREA -- faster, lower quality
## or cv2.INTER_CUBIC -- slower but higher quality

def resize(image):
    resized = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('resized', resized)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def crop(image):
    cropped = image[100:200, 200:500]
    cv2.imshow('cropped', cropped)

    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

colorBg()
drawLines()
writeText()
picPretty()
resize(img)


#
# class shapeChanger():
#     def __init__(self, loc):
#         self.cv2 = cv2.imread(str(loc))
#         self.window = cv2.namedWindow(loc)
#
#     def reSize(self):
#         resized = cv2.resize(self.cv2, (500, 500), interpolation=cv2.INTER_AREA)
#         cv2.imshow('resized by c;ass', resized)
#         cv2.waitKey(5000)
#         if cv2.waitKey(5000) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             return resized
#
#     def Crop(self):
#         cropped = self.cv2[100:200, 200:500]
#         cv2.imshow('cropped by c;ass', cropped)
#
#         cv2.waitKey(5000)
#         if cv2.waitKey(5000) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             return cropped
#
# pic_loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/patric.gif"
# manip = shapeChanger(pic_loc)
# manip.reSize()
# manip.Crop()
#


# manip.reSize(colorBg())



