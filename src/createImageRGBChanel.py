from cv2 import imread, imwrite
from random import randint

def createImageRGBChanel(path, chanel="RED"):
    """
    Функция генерирующая красный, зелёный или синий канал изображения
    
    path - путь к исходному изображению
    filename - имя файла под которым сохраняется новое изображение
    chanel - канал изображения
    
    return filename - путь до нового файла
    """
    hash_ = [str(randint(0, 9)) for i in range(6)]
    hash_ = "".join(hash_)
    
    img = imread(path)
    
    if chanel == "RED":
        filename = f"../imgs/RC/RC{hash_}.png"
        
        img[:, :, 0] = 0
        img[:, :, 1] = 0
        
    elif chanel == "GREEN":
        filename = f"../imgs/GC/GC{hash_}.png"
        
        img[:, :, 0] = 0
        img[:, :, 2] = 0
        
    elif chanel == "BLUE":
        filename = f"../imgs/BC/BC{hash_}.png"
        
        img[:, :, 1] = 0
        img[:, :, 2] = 0
    
    imwrite(filename, img)
    
    return filename
