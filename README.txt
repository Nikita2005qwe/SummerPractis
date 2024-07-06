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
pip install -r requirements.txt

возможная проблема:
error: externally-managed-environment

для её решения попробуйте несколько методов:

1.1 создать окружение и после этого выполнить установку

python -m venv PractisVenv
source PractisVenv/bin/activate
pip install -r requirements.txt

1.2 Используйте pipx

sudo apt install pipx
pipx install -r requirements.txt

1.3 добавление флага --break-system-packages

pip install -r requirements.txt --break-system-packages

2. Перейдите в папку src:
cd src

3. Для запуска приложения в своём терминале выполните команду:
python main.py

Обратите внимание, что путь к файлу main.py не должен содержать кириллицы
