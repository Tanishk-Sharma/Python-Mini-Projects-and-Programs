##############################################################################################################################################################################
# Word Scrambling                                                                                                                                                            #
#                                                                                                                                                                            #
# INTRODUCTION                                                                                                                                                               #
# --------------                                                                                                                                                             #
# The project is to write a Python program that reads a text file, scrambles the words in the file on following rules and writes the output to a new text file:              #
#                                                                                                                                                                            #
# - Words less than or equal to 3 characters need not be scrambled                                                                                                           #
# - Don't scramble first and last char, so Scrambling can become Srbmnacilg or Srbmnailcg or Snmbracilg , i.e. letters except first and last can be scrambled in any order   #
# - Punctuation at the end of the word to be maintained as is i.e. "Surprising," could become "Spsirnirug," but not "Spsirn,irug"                                            #
# - Following punctuation marks are to be supported - Comma Question mark, Full stop, Semicolon, Exclamation                                                                 #
# - Do this for a file and maintain sequences of lines                                                                                                                       #
# - On executing the program, it should prompt the user to enter input file name and generate an output file with scrambled text.                                            #
# - Output file should be named by appending the word "Scrambled" to input file name.                                                                                        #
#                                                                                                                                                                            #
# - The project provides a practice on following concepts to learners:                                                                                                       #
#                                                                                                                                                                            #
# - For loops                                                                                                                                                                #
# - If-else statements                                                                                                                                                       #
# - String                                                                                                                                                                   #
# - Lists                                                                                                                                                                    #
# - Functions                                                                                                                                                                #
# - File operations                                                                                                                                                          #
##############################################################################################################################################################################

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
