from random import shuffle


def pcatend(word):
    puncs = [',', '?', '.', ';', '!']
    if word[-1] in puncs:
        return 1
    else:
        return 0
    
def scrambler(word):
    while (1):
        l1 = list(range(len(word)))
        l2 = l1[:]
        shuffle(l2)
        s = list(word)
        for pos1, pos2 in zip(l1, l2):
            temp = s[pos1]
            s[pos1] = s[pos2]
            s[pos2] = temp
            newstr = "".join(s)
            if newstr != word:
                return newstr
            
inp = input('Input File Name: ')
f1 = open(inp)
lines = f1.readlines()

for l in range(len(lines)):
    words = lines[l].split()
    s = []
    for i in range(len(words)):
        w = words[i]
        if pcatend(w) == 1 and len(w) > 4:
            words[i] = w[0] + scrambler(w[1:-2]) + w[-2:]
        elif pcatend(w) == 0 and len(w) > 3:
            words[i] = w[0] + scrambler(w[1:-1]) + w[-1]
        s.append(words[i] + ' ')
    lines[l] = "".join(s) + '\n'

f1.close()
output = 'Scrambled ' + inp

f2 = open(output, 'w')
f2.write("".join(lines))
f2.close()
