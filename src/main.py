# Точка входа в приложение
from PyQt5 import QtWidgets
from menu import UiMainWindow
import logging
import sys

def declareСonfig():
    """
    Функция задающая basicConfig для всей программы
    """
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.DEBUG, 
                    filename="../logs/InfoLogs.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

if __name__ == "__main__":
    declareСonfig()
    logging.info("Программа начала выполнение")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
