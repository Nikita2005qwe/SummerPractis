from SettingsMenu import SettingsMenu
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui
from cameraFunction import make_screen
from increaseBrightness import increaseBrightness
from createCopyImg import createCopyImg
from createImageRGBChanel import createImageRGBChanel
from cropImage import cropImage
from drawCircle import drawCircle
import logging

class UiMainWindow(SettingsMenu):
    
    """
    Класс добавляющий функционал кнопкам из класса SettingsMenu
    
    По умолчанию методы возвращают 0
    В случае ошибок возвращают -1
    """
    
    def add_functions(self):
        """
        Метод привязывающий функции к кнопкам
        """
        
        logging.info("Связывание функций с кнопками")
        self.screen_image.clicked.connect(lambda: self.makeScreen())
        self.load_image.clicked.connect(lambda: self.loadImage())
        self.btn_increase_brightness.clicked.connect(
            lambda: self.increaseBrightness())
        self.show_rgb_chanel.clicked.connect(lambda: self.showRGBChanel())
        self.show_cropped_img.clicked.connect(lambda: self.cutImage())
        self.set_size.clicked.connect(lambda: self.setMaxSize())
        self.horisontal_spin.valueChanged.connect(
            lambda: self.changeMaximumImageLength())
        self.vertical_spin.valueChanged.connect(
            lambda: self.changeMaximumImageWidth())
        self.show_circle.clicked.connect(lambda: self.drawCircle())
        logging.info("Связывание функций с кнопками завершено")
        return 0
        
        
    def limitSizes(self, length:int, width:int):
        """
        При изменении изображения в label_photo устанавливаются лимиты 
        на значения spins
        length:int - максимальная длинна изображения
        width:int - максимальная ширина изображения
        """
        
        self.width_spin.setMaximum(width)
        self.length_spin.setMaximum(length)
        
        self.vertical_spin.setMaximum(width-1)
        self.horisontal_spin.setMaximum(length-1)
        
        self.vertical_spin_2.setMaximum(width)
        self.horisontal_spin_2.setMaximum(length)
        
        self.radius_spin.setMaximum(width//2)
        self.depth_spin.setMaximum(width//4)
        logging.info("Ограничение значений spins завершено")
        return 0
    
    def showErrors(self, text:str):
        """
        Метод выводящий сообщение об ошибке на экран пользователям
        
        text:str - сообщение об ошибке
        """
        
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.exec_()
        
        return 0
    
    def makeScreen(self):
        """
        Метод создающий изображение с web-camera
        
        msg:QMessageBox - сообщение при нажатии на кнопку
        fileName:str - переменная содержащая путь к произведённому изображению
        """
        
        msg = QMessageBox()
        msg.setWindowTitle("Создание изображения")
        msg.setText("Чтобы сделать снимок нажмите esc")
        msg.exec_()
        fileName = make_screen()
        if fileName == -1:
            self.showErrors("Нет доступа к вебкамере")
            logging.debug("Веб-камера не подключена, что вызвало исключение")
            return -1
        screen = QtGui.QPixmap(fileName)
        self.label_photo.setGeometry(QtCore.QRect(70, 120, 557, 477))
        self.label_photo.setPixmap(screen)
        self.limitSizes(557, 477)
        
        self.currentImage = fileName
        self.isImgImported = True
        
        logging.info("Создано изображение при помощи камеры,"
                     f" сохранено в {fileName}")
        return 0
    
    def loadImage(self):
        """
        Метод импортирующий изображение с диска
        (создаёт копию в папке img/origin)
        
        fileName:str - переменная содержащая путь к изображению
        """
        
        fileName, _ = QFileDialog.getOpenFileName(
            None,"Выбрать изображение","../imgs","Image (*.png *.jpg *.jpeg)")
        if fileName=='':
            self.showErrors("Изображение не выбрано")
            logging.debug("Изображение не выбрано, что вызвало исключение")
            return -1
        logging.info(f"Загруженно изображение, из {fileName}")
        fileName = createCopyImg(fileName)
        screen = QtGui.QPixmap(fileName)
        x, y, w, h = screen.rect().getCoords()
        if w > 1330:
            w = 1330
        if h > 800:
            h = 800
        self.label_photo.setGeometry(QtCore.QRect(70, 120, w, h))
        self.label_photo.setPixmap(screen)
        self.limitSizes(w, h)
        
        self.currentImage = fileName
        self.isImgImported = True
        
        logging.info(f"Загруженное изображение, сохранено в {fileName}")
        return 0
    
    def showRGBChanel(self):
        """
        Метод который передаёт красный синий или зелёный канал
        выбранного изображения
        
        fileName - путь к итоговому изображению
        color - цветовой канал
        """
        if not(self.isImgImported):
            self.showErrors("Изображение не импортированно")
            logging.debug("Изображение не выбрано, что вызвало исключение")
            return -1
        
        fileName = self.currentImage
        
        if self.red_chanel.isChecked():
            color = "RED"
            fileName = createImageRGBChanel(self.currentImage, color)
        elif self.green_chanel.isChecked():
            color = "GREEN"
            fileName = createImageRGBChanel(self.currentImage, color)
        elif self.blue_chanel.isChecked():
            color = "BLUE"
            fileName = createImageRGBChanel(self.currentImage, color)
        else:
            logging.debug("Цветовой канал не был выбран,"
                          " что вызвало исключение")
            self.showErrors("Цветовой канал не был выбран")
            return -1
        
        self.currentImage = fileName
        screen = QtGui.QPixmap(fileName)
        self.label_photo.setPixmap(screen)
        
        logging.info("Метод передающий цветовой канал изображения "
                     "завершён"
                     f"(переданный канал - {color}),"
                     " сохранено в {fileName}")
        
        return 0
    
    def cutImage(self):
        """
        Метод который обрезает изображение по заданным 
        length, width и vertical, horisontal
        
        self.length_spin.value(), self.width_spin.value() - значения
        длинны и ширины нового изображения соответственно
        img - обрезанное изображение
        fileName - путь к итоговому изображению
        """
        
        if not(self.isImgImported):
            self.showErrors("Изображение не импортированно")
            logging.debug("Изображение не выбрано, что вызвало исключение")
            return -1
        if self.length_spin.value() * self.width_spin.value() == 0:
            self.showErrors("Длинна или ширина изображения не могут быть 0")
            logging.debug("Выбранные значения не корректны "
                          f"(length={self.length_spin.value()}, "
                          f"width={self.width_spin.value()})")
            return -1
        
        fileName = cropImage(
            self.currentImage,
            self.horisontal_spin.value(),
            self.vertical_spin.value(),
            self.length_spin.value(),
            self.width_spin.value()
            )
        
        img = QtGui.QPixmap(fileName)
        self.label_photo.setGeometry(
            QtCore.QRect(70, 120,
                         self.length_spin.value(),self.width_spin.value()))
        self.label_photo.setPixmap(img)
        self.currentImage = fileName
        
        logging.info("Метод обрезки изображения завершён "
                     f"(length={self.length_spin.value()}, "
                     f"width={self.width_spin.value()},"
                     f"vertical={self.vertical_spin.value()},"
                     f"horisontal={self.horisontal_spin.value()})"
                     f" сохранено в {fileName}")
        
        self.limitSizes(self.length_spin.value(),
                        self.width_spin.value())
        
        for i in [self.vertical_spin,
                  self.horisontal_spin,
                  self.length_spin,
                  self.width_spin]:
            i.setProperty("value", 0)
        
        return 0
    
    def increaseBrightness(self):
        """
        Метод который делает изображение светлее
        
        self.horizontalSlider.value() - значение horizontalSlider
        показывает на сколько светлым будет изображение (от 1 до 255)
        img - осветлённое изображение
        fileName - путь к итоговому изображению
        """
        
        if not(self.isImgImported):
            logging.debug("Изображение не импортированно,"
                          " что вызвало исключение")
            self.showErrors("Изображение не импортированно")
            return -1
        if self.horizontalSlider.value() == 0:
            logging.debug("Процент яркости не выбран, что вызвало исключение")
            self.showErrors("Процент яркости не был выбран")
            return -1
        
        fileName = increaseBrightness(self.currentImage,
                                      self.horizontalSlider.value())
        img = QtGui.QPixmap(fileName)
        self.currentImage = fileName
        
        self.label_photo.setPixmap(img)
        logging.info("Метод повышения яркости завершён "
                     f"(value={self.horizontalSlider.value()}),"
                     f" сохранено в {fileName}")
        
        self.horizontalSlider.setProperty("value", 0)
        
        return 0
    
    def drawCircle(self):
        """
        Метод который наносит на изображение красную окружность
        с заданными координатами
        
        self.horisontal_spin_2.value() - значение координаты центра 
        по горизонтали
        self.vertical_spin_2.value() - значение координаты центра 
        по вертикали
        self.radius_spin.value() - значение радиуса окружности
        self.depth_spin.value() - значение толщины окружности
        COLOR_CIRCLE - цвет окружности (Красный)
        img - итоговому изображение
        fileName - путь к итоговому изображению
        """
        if not(self.isImgImported):
            self.showErrors("Изображение не импортированно")
            logging.debug("Изображение не импортированно,"
                          " что вызвало исключение")
            return -1
        if self.radius_spin.value() == 0:
            self.showErrors("Радиус окржности не может быть 0")
            logging.debug("Указан радиус окружности 0,"
                          " что вызвало исключение")
            return -1
        if self.depth_spin.value() == 0:
            self.showErrors("Толщина окржности не может быть 0")
            logging.debug("Указана толщина окружности 0,"
                          " что вызвало исключение")
            return -1
        
        COLOR_CIRCLE = (0, 0, 255)
        
        fileName = drawCircle(self.currentImage,
                              (self.horisontal_spin_2.value(), 
                               self.vertical_spin_2.value()),
                              self.radius_spin.value(), COLOR_CIRCLE,
                              self.depth_spin.value()
                              )
        img = QtGui.QPixmap(fileName)
        self.currentImage = fileName
        
        self.label_photo.setPixmap(img)
        
        logging.info(
            "Метод Рисования окружности завершён "
            f"(center="
            f"{(self.vertical_spin_2.value(),self.horisontal_spin_2.value())}"
            f", radius={self.radius_spin.value()}, "
            f"depth={self.depth_spin.value()}, "
            f"color=(0,0,255)),"
            f" сохранено в {fileName}")
        
        for i in [self.vertical_spin_2,
                  self.horisontal_spin_2,
                  self.radius_spin,
                  self.depth_spin]:
            i.setProperty("value", 0)
        
        return 0
    
    def setMaxSize(self):
        """
        Метод который по нажатию на кнопку "Установить максимальные размеры"
        устанавливает максимальные доступные размеры
        длинны и ширины обрезаемого изображения
        """
        
        if not(self.isImgImported):
            logging.debug("Изображение не импортированно,"
                          " что вызвало исключение")
            self.showErrors("Изображение не импортированно")
            return -1
        
        self.length_spin.setProperty("value", self.length_spin.maximum())
        self.width_spin.setProperty("value", self.width_spin.maximum())
        return 0
    
    def changeMaximumImageLength(self):
        """ 
        При изменении значения self.horisontal_spin.value() значение
        self.length_spin так же изменяется на столько же пунктов
        
        max_val - предыдущая максимальная длинна обрезанного изображения
        val - текущее значение self.horisontal_spin
        old_val - предыдущее значение self.horisontal_spin
        
        new_max_val - новое максимальное значение
        длинны обрезанного изображения
        """
        max_val = self.length_spin.maximum()
        val = self.horisontal_spin.value()
        old_val = self.old_horisontal_spin
        
        new_max_val = max_val - (val - old_val)
        
        self.length_spin.setMaximum(new_max_val)
        self.old_horisontal_spin = self.horisontal_spin.value()
        
    def changeMaximumImageWidth(self):
        """ 
        При изменении значения self.vertical_spin.value() значение
        self.width_spin так же изменяется на столько же пунктов
        
        max_val - предыдущая максимальная ширина обрезанного изображения
        val - текущее значение self.vertical_spin
        old_val - предыдущее значение self.vertical_spin
        
        new_max_val - новое максимальное значение
        ширины обрезанного изображения
        """
        
        max_val = self.width_spin.maximum()
        val = self.vertical_spin.value()
        old_val = self.old_vertical_spin
        
        new_max_val = max_val - (val - old_val)
        
        self.width_spin.setMaximum(new_max_val)
        self.old_vertical_spin = self.vertical_spin.value()
        
        