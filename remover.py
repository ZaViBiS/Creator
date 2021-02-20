# Этот срипт удаляет файлы используя 'log.txt'

import os

l = []
for x in open('log.txt'):
    l.append(x)
l = [line.rstrip() for line in l]

for x in l:
    os.remove(x)

os.remove('log.txt')
