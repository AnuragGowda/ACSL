# Kinda Oneliner
for line in list(open('inputs.txt', 'r').readlines()): word1, word2, run, reset, off = list(line.split()[0]), list(line.split()[1]), False, lambda x: exec('global run; run=True'), lambda x: exec('global run; run=False'); [[[[[[[word1.pop(i),word2.pop(i), reset(run)] for i in blah if i < len(word1) and i < len(word2) and word1[i]==word2[i]], [[off(run)] for i in blah if (run and i+1 < len(word2) and i < len(word1) and word1[i]==word2[i+1] and word2.pop(i)) or (run and i+1 < len(word1) and i < len(word2) and word1[i+1]==word2[i] and word1.pop(i))]] for i in range(10)], print(sum([ord(word1[i])-ord(word2[i]) for i in range(min(len(word1),len(word2)))]+[max(len(word1),len(word2))-min(len(word1),len(word2))]))] for i in range(1)] for blah in [[int(i) for i in ''.join([(str(i)+' ')*(len(word1)-i) for i in [i for i in range(len(word1))]]).split()]]]

'''
I think this one was much trickier to oneline...
also I used a semi-colon (im not counting the lambda ones cause they are strings lol) but I couldve just made them all loop vars
for exaple if I had a var word1 = list('string'); word1.pop(1); print(word1), I can just simplify to:
[[word1.pop(1), print(word1)] for word1 in [list('string')]] thus elimiating all semi-colons
furthermore, to run this and something else once, I just do:
[[SOME OTHER CODE, [[word1.pop(1), print(word1)] for word1 in [list('string')]]] for i in range(1)] <- how to abuse list comprehension btw
and therefore I can eliminate any semi-colons. However, this would take too long so I just left the one I had.
'''

# Code Simplified
'''
for line in list(open('inputs.txt', 'r').readlines()):
word1 = list(line.split()[0])
word2 = list(line.split()[1])
run = False
reset = lambda x: exec('global run; run=True')
off = lambda x: exec('global run; run=False')

[[[[[[[word1.pop(i),word2.pop(i), reset(run)] for i in blah if i < len(word1) and i < len(word2) and word1[i]==word2[i]], [[off(run)] for i in blah if (run and i+1 < len(word2) and i < len(word1) and word1[i]==word2[i+1] and word2.pop(i)) or (run and i+1 < len(word1) and i < len(word2) and word1[i+1]==word2[i] and word1.pop(i))]] for i in range(10)], print(sum([ord(word1[i])-ord(word2[i]) for i in range(min(len(word1),len(word2)))]+[max(len(word1),len(word2))-min(len(word1),len(word2))]))] for i in range(1)] for blah in [[int(i) for i in ''.join([(str(i)+' ')*(len(word1)-i) for i in [i for i in range(len(word1))]]).split()]]]


'''
