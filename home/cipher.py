
a = ('X...',
     '..X.',
     'X..X',
     '....')

b = ('itdf',
     'gdce',
     'aton',
     'qrdi')


def recall_password(a, b):
    cc = []
    cc.append(list(a))

    def convert(l):
        c = []
        for i in range(len(l)):
            s = []
            for z in reversed(l):
                s.append(z[i])
            c.append(''.join(s))
        cc.append(c)
        if len(cc) == 4:
            return
        convert(c)

    convert(list(a))

    ret = ''
    for qq in cc:
        for q_index, q in enumerate(qq):
            for s_index, s in enumerate(list(q)):
                if s == 'X':
                    ret += b[q_index][s_index]

    return ret

if __name__ == '__main__':
    recall_password(a=a, b=b)
