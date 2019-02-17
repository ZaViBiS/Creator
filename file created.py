print('0%')
import random
print('50%')
import string
print('100%')
ti = int(input('1 - on time sleep\n2 - off time sleep\n: '))
Ksdh = "import random, string\npas = input('you password : ')\ns = 0\nwhile True:\n    rt = random.random()\n    b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1))\n    print('fell out - ', b)\n    if b == pas:\n		print('you win\nto guess the password' , s , 'was gone attempts' )\n		break\n	   s += 1\ninput('clik to close prog...')"
loginer = "login = input('login: ')\nif login == 'admin':\n    password = input('password: ')\n    if password == 'n':\n        print('ok')\n        input('press Enter to close the program...')\n    else:\n        print()#break\nelse:\n    input()#break"
ziper = "import zipfile, os\nwith zipfile.ZipFile('spam.rar', 'w') as myzip:\n    myzip.write('1Ucl.py')\n# it's spam file!"
if ti == 1:
    while True:
        import time
        rt = random.random()
        b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.py'
        print('file', b ,'successfully created')
        rp = random.randint(1, 3)
        if rp == 1:
            sav = Ksdh
        elif rp == 2:
            sav = loginer
        elif rp == 3:
            sav = ziper
        else:
            pass
        f = open(b, 'w')
        f.write(sav)
        f.close()
        time.sleep(rt)
elif ti == 2:
    while True:
        rt = random.random()
        b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.py'
        print('file', b ,'successfully created')
        rp = random.randint(1, 3)
        if rp == 1:
            sav = Ksdh
        elif rp == 2:
            sav = loginer
        elif rp == 3:
            sav = ziper
        else:
            pass
        f = open(b, 'w')
        f.write(sav)
        f.close()
else:
    pass
