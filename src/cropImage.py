from cv2 import imread, imwrite
from random import randint

def cropImage(path, horisontal, vertical, length, width):
    """
    Функция обрезающая изображение
    
    path - путь к исходному изображению
    horisontal, vertical - координаты левого верхнего угла
    возвращаемого изображения
    length, width - длинна и ширина возвращаемого изображения
    hash_ - случайный код для изображения
    
    return f"../imgs/CD/CD{hash_}.png" - путь к изображению
    """
    
    hash_ = [str(randint(0, 9)) for i in range(6)]
    hash_ = "".join(hash_)
    filename = f"../imgs/CD/CD{hash_}.png"
    
    img = imread(path)
    
    img = img[vertical:vertical+width, horisontal:horisontal+length]
    
    imwrite(filename, img)
    
    return filename
