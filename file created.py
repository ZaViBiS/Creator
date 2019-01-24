import random, string, time
while True:
    rt = random.random()
    r = random.choice((4, 4))
    b = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)) + '.py'
    print('file', b ,'successfully created')
    f = open(b, 'w')
    time.sleep(rt)
