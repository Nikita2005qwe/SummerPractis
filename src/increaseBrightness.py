from cv2 import (imread, imwrite, cvtColor,
                 COLOR_BGR2HSV, COLOR_HSV2BGR, split, merge)
from random import randint

def increaseBrightness(path, brightness_percentage):
    """
    Функция которая длеает изображение более ярким
    
    path - путь до исходного файла
    filename - имя файла под которым сохраняется новое изображение
    brightness_percentage - процент яркости
    на который будет увеличен каждый пиксель
    
    return f"../imgs/BN/{hash_}" - путь до нового файла
    """
    
    hash_ = [str(randint(0, 9)) for i in range(6)]
    hash_ = "".join(hash_)
    filename = f"../imgs/BN/BN{hash_}.png"
    
    img = imread(path)
    
    hsv = cvtColor(img, COLOR_BGR2HSV)
    h, s, v = split(hsv)
    lim = 255 - brightness_percentage
    v[v > lim] = 255
    v[v <= lim] += brightness_percentage
    final_hsv = merge((h, s, v))
    img = cvtColor(final_hsv, COLOR_HSV2BGR)
    
    imwrite(filename, img)
    
    return filename
