'''
# --- Переменные --- #
tree # Путя ко всем дерикториям
data # Данные для записи в файл
file_name # Имя файла
content_selection # Выбор содержимого файла

'''

import cfg
import func
import time
import string
import random
import colorama
import os.path
from sys import argv

# --- Иницализация colorama --- #
colorama.init()

# --- Переменные --- #
tree = func.tree() # Путя ко всем дерикториям
room = 0 # 
yes_or_not, sec = func.arg(argv)
road = [] # Путя к созданым файлам


# --- ^ main ^ --- #
while True:
    # --- Генерация имени файла --- #
    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.' + cfg.after_point[random.randint(0, len(cfg.after_point) - 1)]

    # --- ^ - ^ --- #
    print('File', colorama.Fore.CYAN + file_name, colorama.Style.RESET_ALL + 'successfully created')
    # --- />_</ --- #

    # --- Выбор содержимого файла --- #
    content_selection = random.randint(1, 3)
    if content_selection == 1:
        data = cfg.Ksdh
    elif content_selection == 2:
        data = cfg.loginer
    elif content_selection == 3:
        data = cfg.ziper

    # --- Создание и запись в файл --- #
    if cfg.where == 'here': # Записывать файл в рандомном месте или нет
        open(file_name, 'w').write(data)
        road = (os.path.abspath('') + '\\' + file_name)
    else: # да, в рандомном
        open(tree[room] + '\\' + file_name, 'w').write(data)
        road = (tree[room] + '\\' + file_name)
        room += 1

    # --- Запись в log файл --- #
    if cfg.log.upper() != 'NO':
        f = open('log.txt', 'a+').write(road + '\n')


    # -\^/- Активация задержик ( если надо ) -\^/- #
    if yes_or_not.upper() != 'NO':
        if sec != None:
            time.sleep(sec)
        else:
            time.sleep(1)

