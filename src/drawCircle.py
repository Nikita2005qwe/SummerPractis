from cv2 import circle, imread, imwrite
from random import randint

def drawCircle(path, centerCoords, radius, color, depth):
    """
    Функция котороя рисует окружность в заданном центре
    с заданным цветом, толщиной и радиусом
    
    path - путь к исходному изображению
    centerCoords - кортеж координат центра окружности
    radius - значение радиуса окружности
    color - цвет в формате RGB
    depth - значение толщины окружности
    
    return filename - путь до нового файла
    """
    
    hash_ = [str(randint(0, 9)) for i in range(6)]
    hash_ = "".join(hash_)
    filename = f"../imgs/DC/DC{hash_}.png"
    
    img = imread(path)
    
    circle(img, centerCoords, radius, color, depth)
    
    imwrite(filename, img)
    
    return filename
