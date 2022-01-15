

'''
    * Used for preprocessing images/img data. 
    * Best Optimized for text documents taken in low-light conditions. 
    
'''


class Image_Parser(loc):
    import cv2
    def __init__(self, loc):
        self.loc = loc

    @classmethod
    def from_input(cls):
        return cls(loc = input('Enter Stock: '))

    def rescaleFrames(frame, scale=1.25):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)  # set tuple for return
        print(f'[+] Dimensions :: [{width}] x [{height}] :: [+]')
        return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


    def img_threshing(self):

        ''' Will read img, then perform thresholding / adaptive thresholding, then display the image '''

        img = cv2.imread(str(self.loc))
        img = cv2.cv2Color(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img(560, 900))
        cv2.namedWindow("Original")

        ## set cv2 threshold
        _, Thresh_Binary = cv2.threshold(img, 20, 255, cv2.THRES_BINARY)
        cv2.namedWindow("Thresh_Binary")

        _, Thresh_Binary_Inv = cv2.threshold(img, 20, 255, cv2.THRES_BINARY_INV)
        cv2.namedWindow("Thresh_Binary_Inv")

        _, Thresh_Trunc = cv2.threshold(img, 20, 255, cv2.THRES_TRUNC)
        cv2.namedWindow("Thresh_Trunc")

        _, Thresh_To_Zero = cv2.threshold(img, 20, 255, cv2.THRESH_TOZERO)
        cv2.namedWindow("Thresh_To_Zero")

        _, Thresh_To_Zero_Inv = cv2.threshold(img, 20, 255, cv2.THRESH_TOZERO_INV)
        cv2.namedWindow("Thresh_To_Zero_Inv")


        ## Use adaptive thresholidng to maintain consistant thresholding
        Adaptive_Thresh_Binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_,
                                                cv2.THRES_BINARY, 41, 5)  ## THRES_BINARY
        cv2.namedWindow("Adaptive_Thresh_Binary")

        Adaptive_Thres_Binary_Inv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_,
                                                cv2.THRES_BINARY_INV, 41, 5)  ## THRES_TRUNC
        cv2.namedWindow("Adaptive_Thresh_Binary_Inv")

        Adaptive_Adapt_Gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_,
                                                cv2.THRES_TRUNC, 41, 5)  ## THRESH_TOZERO
        cv2.namedWindow("Thresh_Trunc")

        Adaptive_To_Zero= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_,
                                                cv2.THRESH_TOZERO, 41, 5)  ## THRESH_TOZERO_INV
        cv2.namedWindow("Adaptive_Thresh_To_Zero")

        Adaptive_To_Zero_Inv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_,
                                                cv2.THRESH_TOZERO_INV, 41, 5)  ## THRESH_TOZERO_INV
        cv2.namedWindow("Adaptive_Thresh_To_Zero_Inv")

    def display_img(self):
        ''' Display Images '''

        # Oringal Image
        cv2.imshow('Original', img)

        # Applied Thresholding
        cv2.imshow('Thresh_Binary', Thresh_Binary)
        cv2.imshow('Thresh_Binary_Inv', Thresh_Binary_Inv)
        cv2.imshow('Thresh_Trunc', Thresh_Trunc)
        cv2.imshow('Thresh_To_Zero',Thresh_To_Zero)
        cv2.imshow('Thresh_To_Zero_Inv', Thresh_To_Zero_Inv)

        # Adaptive Thresholding
        cv2.imshow('Adaptive_Thresh_Binary', Adaptive_Thresh_Binary)
        cv2.imshow('Adaptive_Thresh_Binary_Inv', Adaptive_Thresh_Binary_Inv )
        cv2.imshow('Thresh_Trunc', Thresh_Trunc )
        cv2.imshow('Adaptive_Thresh_To_Zero', Adaptive_Thresh_To_Zero )
        cv2.imshow('Adaptive_Thresh_To_Zero_Inv', Adaptive_Thresh_To_Zero_Inv )

        ## kill process
        cv2.waitKey(0)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return loc, img
        cv2.destroyAllWindows()
        return loc, img


def main():
    loc = Image_Parser.from_input()
    loc.img_threashing()

#if '__name__' == '__main__':
main()


