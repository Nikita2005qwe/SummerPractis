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

1. Установите необходимые зависимости:
pip3 install -r requirements.txt

возможная проблема:
error: externally-managed-environment

для её решения воспользуйтесь следующим методом:

удебитесь что у вас установлен python3-venv:
sudo apt install python3-venv

создайте окружение и после этого выполните установку

python3 -m venv PractisVenv
source PractisVenv/bin/activate
pip3 install -r requirements.txt

2. Перейдите в папку src:
cd src

3. Для запуска приложения в своём терминале выполните команду:
python3 main.py

Обратите внимание, что путь к файлу main.py не должен содержать кириллицы
