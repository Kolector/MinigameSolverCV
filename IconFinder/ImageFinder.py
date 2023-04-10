import cv2 as cv
import numpy as np

area_img = cv.imread('FindHere.png', cv.IMREAD_ANYCOLOR)
toolbox_img = cv.imread('FindThisCropped.png', cv.IMREAD_ANYCOLOR)

result = cv.matchTemplate(area_img, toolbox_img, cv.TM_CCOEFF_NORMED) #TM_COERR_NORMED

# Находим размер картинки для поиска
toolbox_w = toolbox_img.shape[1]
toolbox_h = toolbox_img.shape[0]

# Получим позиции по совпадением больше чем порог

threshold = 0.7
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))
#print(locations)

# Группировка совпадений, которые стоят рядом (03)

rectangles = []
for loc in locations:
    rect = [int(loc[0]), int(loc[1]), toolbox_w, toolbox_h]
    rectangles.append(rect)

rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
print(rectangles)

# Поиск всех тулбоксов по совпадением > чем порог (02)
if len(rectangles):
    print('Found image.')

    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:
        # Определяем координаты на экране для отрисовки прямоугольника
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        # Отрисовка прямоугольника
        cv.rectangle(area_img, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches', area_img)
    cv.waitKey()

else:
    print('Image not found.')


# получим позицию лучшего совпадения

#min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

#print('Best match top left position: %s' % str(max_loc))
#print('Best match confidence: %s' % max_val)

#threshold = 0.7
#if max_val >= threshold:
#    print('Found toolbox.')
#
#    toolbox_w = toolbox_img.shape[1]
#    toolbox_h = toolbox_img.shape[0]
#
#    top_left = max_loc
#    bottom_right = (top_left[0] + toolbox_w, top_left[1] + toolbox_h)
#
#    cv.rectangle(area_img, top_left, bottom_right,
#                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
#    
#    cv.imshow('Result', area_img)
#    cv.imwrite('FoundYa.jpg', area_img)
#    cv.waitKey() 
#else:
#    print('Toolbox not found.')







   