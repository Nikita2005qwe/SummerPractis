from PyQt5 import QtCore, QtGui, QtWidgets
import logging


class SettingsMenu(object):
    
    """
    Класс описывающий расположение виджетов, а так же надписи на них и шрифты
    """
    
    def setupUi(self, MainWindow):
        """
        Метод задающий начальное расположение виджетов в окне
        """
        logging.info("Создание окна")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(10, 10, 260, 40))
        self.load_image.setFont(font)
        self.load_image.setObjectName("load_image")
        
        self.screen_image = QtWidgets.QPushButton(self.centralwidget)
        self.screen_image.setGeometry(QtCore.QRect(320, 10, 400, 40))
        self.screen_image.setFont(font)
        self.screen_image.setObjectName("screen_image")
        
        self.label_photo = QtWidgets.QLabel(self.centralwidget)
        self.label_photo.setGeometry(QtCore.QRect(70, 120, 1330, 800))
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        
        self.red_chanel = QtWidgets.QRadioButton(self.centralwidget)
        self.red_chanel.setGeometry(QtCore.QRect(1450, 50, 200, 30))
        self.red_chanel.setFont(font)
        self.red_chanel.setObjectName("red_chanel")
        
        self.blue_chanel = QtWidgets.QRadioButton(self.centralwidget)
        self.blue_chanel.setGeometry(QtCore.QRect(1450, 130, 200, 30))
        self.blue_chanel.setFont(font)
        self.blue_chanel.setObjectName("blue_chanel")
        
        self.green_chanel = QtWidgets.QRadioButton(self.centralwidget)
        self.green_chanel.setGeometry(QtCore.QRect(1450, 90, 200, 30))
        self.green_chanel.setFont(font)
        self.green_chanel.setObjectName("green_chanel")
        
        for i in (self.red_chanel, self.blue_chanel, self.green_chanel):
            i.setEnabled(True)
            i.setChecked(False)
        
        self.label_change_chanel = QtWidgets.QLabel(self.centralwidget)
        self.label_change_chanel.setGeometry(QtCore.QRect(1450, 0, 380, 50))
        self.label_change_chanel.setFont(font)
        self.label_change_chanel.setObjectName("label_change_chanel")
        
        self.show_rgb_chanel = QtWidgets.QPushButton(self.centralwidget)
        self.show_rgb_chanel.setGeometry(QtCore.QRect(1450, 170, 450, 40))
        self.show_rgb_chanel.setFont(font)
        self.show_rgb_chanel.setObjectName("show_rgb_chanel")
        
        self.lebel_set_size = QtWidgets.QLabel(self.centralwidget)
        self.lebel_set_size.setGeometry(QtCore.QRect(1450, 210, 380, 50))
        self.lebel_set_size.setFont(font)
        self.lebel_set_size.setObjectName("lebel_set_size")
        
        self.vertical_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.vertical_spin.setGeometry(QtCore.QRect(1810, 270, 81, 31))
        self.vertical_spin.setMaximum(1080)
        self.vertical_spin.setObjectName("vertical_spin")
        
        self.horisontal_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.horisontal_spin.setGeometry(QtCore.QRect(1585, 270, 81, 30))
        self.horisontal_spin.setMaximum(1920)
        self.horisontal_spin.setObjectName("horisontal_spin")
        
        self.label_vertical = QtWidgets.QLabel(self.centralwidget)
        self.label_vertical.setGeometry(QtCore.QRect(1670, 270, 130, 30))
        self.label_vertical.setFont(font)
        self.label_vertical.setObjectName("label_vertical")
        
        self.label_horisontal = QtWidgets.QLabel(self.centralwidget)
        self.label_horisontal.setGeometry(QtCore.QRect(1450, 270, 130, 30))
        self.label_horisontal.setFont(font)
        self.label_horisontal.setObjectName("label_horisontal")

        self.width_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.width_spin.setGeometry(QtCore.QRect(1810, 310, 80, 31))
        self.width_spin.setMaximum(1080)
        self.width_spin.setObjectName("width_spin")
        
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setGeometry(QtCore.QRect(1450, 310, 130, 30))
        self.label_length.setFont(font)
        self.label_length.setObjectName("label_length")
        
        self.label_width = QtWidgets.QLabel(self.centralwidget)
        self.label_width.setGeometry(QtCore.QRect(1670, 310, 130, 30))
        self.label_width.setFont(font)
        self.label_width.setObjectName("label_width")
        
        self.length_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.length_spin.setGeometry(QtCore.QRect(1585, 310, 80, 30))
        self.length_spin.setMaximum(1920)
        self.length_spin.setObjectName("length_spin")

        self.set_size = QtWidgets.QPushButton(self.centralwidget)
        self.set_size.setGeometry(QtCore.QRect(1450, 350, 450, 40))
        self.set_size.setFont(font)
        self.set_size.setObjectName("set_size")
        
        self.show_cropped_img = QtWidgets.QPushButton(self.centralwidget)
        self.show_cropped_img.setGeometry(QtCore.QRect(1450, 400, 450, 40))
        self.show_cropped_img.setFont(font)
        self.show_cropped_img.setObjectName("show_cropped_img")

        self.btn_increase_brightness = QtWidgets.QPushButton(
            self.centralwidget)
        self.btn_increase_brightness.setGeometry(
            QtCore.QRect(1450, 540, 450, 40))
        self.btn_increase_brightness.setFont(font)
        self.btn_increase_brightness.setObjectName("btn_increase_brightness")

        self.label_increase_brightness = QtWidgets.QLabel(self.centralwidget)
        self.label_increase_brightness.setGeometry(
            QtCore.QRect(1450, 450, 380, 50))
        self.label_increase_brightness.setFont(font)
        self.label_increase_brightness.setObjectName(
            "label_increase_brightness")
        
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(1450, 510, 450, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setPageStep(51)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(51)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        self.lebel_set_coords_center_circle = QtWidgets.QLabel(
            self.centralwidget)
        self.lebel_set_coords_center_circle.setGeometry(QtCore.QRect(
            1450, 590, 380, 50))
        self.lebel_set_coords_center_circle.setFont(font)
        self.lebel_set_coords_center_circle.setObjectName(
            "lebel_set_coords_center_circle")
        
        self.show_circle = QtWidgets.QPushButton(self.centralwidget)
        self.show_circle.setGeometry(QtCore.QRect(1450, 730, 450, 40))
        self.show_circle.setFont(font)
        self.show_circle.setObjectName("show_circle")

        self.vertical_spin_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.vertical_spin_2.setGeometry(QtCore.QRect(1810, 650, 81, 31))
        self.vertical_spin_2.setMaximum(1080)
        self.vertical_spin_2.setObjectName("vertical_spin_2")
        
        self.label_horisontal_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_horisontal_2.setGeometry(QtCore.QRect(1450, 650, 130, 30))
        self.label_horisontal_2.setFont(font)
        self.label_horisontal_2.setObjectName("label_horisontal_2")
        
        self.label_vertical_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_vertical_2.setGeometry(QtCore.QRect(1670, 650, 130, 30))
        self.label_vertical_2.setFont(font)
        self.label_vertical_2.setObjectName("label_vertical_2")
        
        self.horisontal_spin_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.horisontal_spin_2.setGeometry(QtCore.QRect(1585, 650, 81, 30))
        self.horisontal_spin_2.setMaximum(1920)
        self.horisontal_spin_2.setObjectName("horisontal_spin_2")

        self.label_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_radius.setGeometry(QtCore.QRect(1450, 690, 130, 30))
        self.label_radius.setFont(font)
        self.label_radius.setObjectName("label_radius")
        
        self.radius_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_spin.setGeometry(QtCore.QRect(1585, 690, 81, 30))
        self.radius_spin.setMaximum(540)
        self.radius_spin.setObjectName("radius_spin")
        
        self.label_depth = QtWidgets.QLabel(self.centralwidget)
        self.label_depth.setGeometry(QtCore.QRect(1670, 690, 130, 30))
        self.label_depth.setFont(font)
        self.label_depth.setObjectName("label_depth")
        
        self.depth_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.depth_spin.setGeometry(QtCore.QRect(1810, 690, 81, 30))
        self.depth_spin.setMaximum(270)
        self.depth_spin.setObjectName("depth_spin")
        
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(1450, 780, 450, 40))
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        
        logging.info("Создание виджетов завершено")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        def close_app(MainWindow):
            # Функция завершающая выполнение программы
            logging.info("Программа закончила выполнение")
            MainWindow.close()
        
        self.quit_btn.clicked.connect(lambda:close_app(MainWindow))
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.add_functions()
        
        # переменная показывающая загруженно ли изображение в self.label_photo
        self.isImgImported = False 
        
        # путь к текущему загруженному изображению в self.label_photo
        self.currentImage = None
        
        # предыдущее значение self.vertical_spin
        self.old_vertical_spin = 0
        
        # предыдущее значение self.horisontal_spin
        self.old_horisontal_spin = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow","MainWindow"))
        
        self.load_image.setText(
            _translate("MainWindow","Загрузить изображение"))
        
        self.screen_image.setText(
            _translate("MainWindow","Получить изображение с web-camera"))
        
        self.red_chanel.setText(
            _translate("MainWindow","Красный канал"))
        
        self.blue_chanel.setText(
            _translate("MainWindow","Синий канал"))
        
        self.green_chanel.setText(
            _translate("MainWindow","Зелёный канал"))
        
        self.label_change_chanel.setText(
            _translate("MainWindow","Выберите цветовой канал"))
        
        self.lebel_set_size.setText(
            _translate("MainWindow","Введите координаты для обрезки"))
        
        self.show_rgb_chanel.setText(
            _translate("MainWindow","Показать выбранный цветовой канал"))
        
        self.label_vertical.setText(
            _translate("MainWindow","Вертикаль"))
        
        self.label_horisontal.setText(
            _translate("MainWindow","Горизонталь"))
        
        self.label_length.setText(
            _translate("MainWindow","Длинна"))
        
        self.label_width.setText(
            _translate("MainWindow","Ширина"))
        
        self.set_size.setText(
            _translate("MainWindow","Применить максимальные размеры"))
        
        self.show_cropped_img.setText(
            _translate("MainWindow","Обрезать изображение"))
        
        self.btn_increase_brightness.setText(
            _translate("MainWindow","Повысить яркость"))
        
        self.label_increase_brightness.setText(
            _translate("MainWindow","Измените яркость изображения"))
        
        self.lebel_set_coords_center_circle.setText(
            _translate("MainWindow","Введите координаты центра круга"))
        
        self.show_circle.setText(
            _translate("MainWindow","Изобразить круг"))
        
        self.label_horisontal_2.setText(
            _translate("MainWindow","Горизонталь"))
        
        self.label_vertical_2.setText(
            _translate("MainWindow","Вертикаль"))
        
        self.label_radius.setText(
            _translate("MainWindow","Радиус"))
        
        self.label_depth.setText(
            _translate("MainWindow","Толщина"))
        
        self.quit_btn.setText(
            _translate("MainWindow","Выход"))
        
        logging.info("Текст нанесён на виджеты")
    
    def add_functions(self):
        pass
