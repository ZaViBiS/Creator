def tree(dirct='/'):
    from os import walk

    outtss = []
    for x in walk(dirct):
        outtss.append(x[0])

    return outtss
