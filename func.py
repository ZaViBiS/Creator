import cfg

def tree(dirct='/'):
    from os import walk
    if cfg.where == 'here':
        return None
    else:
        outtss = []
        for x in walk(dirct):
            outtss.append(x[0])

        return outtss


def arg(l):
    if len(l) <= 1:
        return 'yes', 0.5
    else:
        yes = l[1]
        if len(l) >= 3:
            sec = float(l[2])
        else:
            sec = 0
        return yes ,sec



