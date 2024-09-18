import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui as gui
import PIL

# Выбираем директорию со скриптом текущей
os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while(True):
    screenshot = gui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    #Нажать q чтобы завершить
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
