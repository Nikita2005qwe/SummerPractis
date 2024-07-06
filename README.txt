Инструкция для Windows:

1. Создайте окружение при помощи conda
conda create -n PractisVenv

2. Активируйте окружение
conda activate PractisVenv

3. Для установки требуемых зависимостей в своём терминале выполните команду:
pip install -r requirements.txt

4. Перейдите в папку src:
cd src

5. Для запуска приложения в своём терминале выполните команду:
python main.py


Инструкция для Linux:

убедитесь что у вас установлен python3-venv:
sudo apt install python3-venv

1.Установите и активируйте виртуальное окружение:
python3 -m venv PractisVenv
source PractisVenv/bin/activate

2. Установите необходимые зависимости:
pip3 install -r req.txt

3. Перейдите в папку src:
cd src

4. Для запуска приложения в своём терминале выполните команду:
python3 main.py

Обратите внимание, что путь к файлу main.py не должен содержать кириллицы
