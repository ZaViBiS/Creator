import random
import string

if choice == 1:
    while True:
        import time
        rt = random.random()
        b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.py'
        print('file', b ,'successfully created')
        content_selection = random.randint(1, 3)
        if content_selection == 1:
            data = Ksdh
        elif content_selection == 2:
            data = loginer
        elif content_selection == 3:
            data = ziper
        f = open(b, 'w')
        f.write(data)
        f.close()
        time.sleep(rt)
elif choice == 2:
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
