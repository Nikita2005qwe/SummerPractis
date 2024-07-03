from cv2 import VideoCapture, destroyAllWindows, imshow, waitKey, imwrite, error
from random import randint
    
def make_screen():
    """
    Функция делающая скриншот и сохраняющая его в папке img/origin
    
    cap - переменная связывающая видеокамеру с приложением
    hash_ - случайный код для изображения
    
    return f"../imgs/origin/screen{string_hash}.png" - путь к изображению
    """
    cap = VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        try:
            imshow("camera", img)
        except error:
            return -1
        if waitKey(1) == 27:
            
            hash_ = [str(randint(0, 9)) for i in range(6)]
            string_hash = "".join(hash_)
            
            imwrite(f"../imgs/origin/screen{string_hash}.png", img)
            break
        
    cap.release()
    destroyAllWindows()
    
    return f"../imgs/origin/screen{string_hash}.png"
