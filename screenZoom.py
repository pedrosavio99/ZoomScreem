#add 4 variaveis que serão as props de top, bottom, esqequerda e dirita
#pip install pillow
#pip install opencv-python

from PIL import ImageGrab
import numpy as np
from PIL import Image
import cv2

while(True):
    img = ImageGrab.grab(bbox=(580,810,1330,1300)) #VAI DE 300 ATE O 800 PX E DE 100 ATE O 800 TBMM
      
    width, height = img.size
    
    left = 2
    top = height / 7
    right = width
    bottom = 3 * height / 14
    
    im1 = img.crop((left, top, right, bottom))
    newsize = (1200, 120)
    im1 = im1.resize(newsize)
        
    
    frame = np.array(im1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.imshow('frame', frame)
    

    if cv2.waitKey(1)==27:
        break


cv2.destroyAllWindows()

