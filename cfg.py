# Содержимое файла
Ksdh = "import random, string\npas = input('you password : ')\ns = 0\nwhile True:\n    rt = random.random()\n    b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1))\n    print('fell out - ', b)\n    if b == pas:\n        print('you win\nto guess the password' , s , 'was gone attempts' )\n        break\n    s += 1\ninput('clik to close prog...')"
loginer = "login = input('login: ')\nif login == 'test':\n    password = input('password: ')\n    if password == 'n':\n        print('ok')\n        input('press Enter to close the program...')\n    else:\n        print()#break\nelse:\n    input()#break"
ziper = "import zipfile, os\nwith zipfile.ZipFile('spam.rar', 'w') as myzip:\n    myzip.write('1Ucl.py')\n# it's spam file!"

# расширения файла
after_point = ['doc', 'docx', 'pdf', 'xls', 'xlsx', 'zip', 'rar', 'mp3', 'mp4', 'mp5', 'jpg', 'gif', 'png', 'ico',
               'flac', 'm4p', 'py', 'cpp', 'h', '7z', 'html', 'js', 'css', 'bpm', 'txt', 'md', 'avi', 'wav', 'ogg', 'mkv', 'dll', 'bin', 'sh']

# Где записывать файл
where = 'here'
log = 'yes'
