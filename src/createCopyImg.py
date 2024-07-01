from PIL import Image
from random import randint

def createCopyImg(path):
    
    """
    Функция создающая копию изображения в папку imgs/origin
    предназначена для того чтобы исправить ошибку связанную с
    названием файлов на кириллице
    
    path - исходный путь к файлу
    
    return filename - возвращаемое значение копии файла в папке imgs/origin
    """
    
    img = Image.open(path)
    
    
    hash_ = [str(randint(0, 9)) for i in range(6)]
    hash_ = "".join(hash_)
    filename = f"../imgs/origin/screen{hash_}.png"
    
    img.save(filename)
    
    return filename
