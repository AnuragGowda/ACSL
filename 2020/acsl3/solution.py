# Got away with using one semicoln... not rly sure how to get rid of it :/
# Hopefully I didn't do smth dumb and the program just crashes lmao that would be super tragic
for line in list(open('inputs.txt', 'r').readlines()): table, correspond, lists, convert = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]], {'A': ['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][1]', '[1][1]', '[2][1]', '[3][1]'],'B': ['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[1][0]', '[1][1]', '[1][2]', '[1][3]'],'C': ['[0][1]', '[1][1]', '[2][1]', '[3][1]', '[0][2]', '[1][2]', '[2][2]', '[3][2]'],'D': ['[1][0]', '[1][1]', '[1][2]', '[1][3]', '[2][0]', '[2][1]', '[2][2]', '[2][3]'],'~A':['[0][2]', '[1][2]', '[2][2]', '[3][2]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],'~B':['[2][0]', '[2][1]', '[2][2]', '[2][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]'],'~C':['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],'~D':['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]']}, [i for i in [[small[i]+small[i+1] for i in range(len(small)) if small[i]=='~']+[small[i] for i in range(len(small)) if (i==0 and small[i]!='~') or (small[i]!='~' and small[i-1]!='~')] for small in list(line.strip().split('+'))]], lambda l, i: exec('lists['+str(l)+']['+str(i)+']=correspond[lists['+str(l)+']['+str(i)+']]');[[[[convert(l,i) for i in range(len(lists[l]))] for l in range(len(lists))], [[[[exec('table'+i+'=1') for i in [i for i in [i for i in lists[0] for l in lists[1:] for x in l if i==x] if [i for i in lists[0] for l in lists[1:] for x in l if i==x].count(i)==len(lists)-1]] for lists in lists], print(''.join([i.upper() if i.isalpha() else i for i in [format(int(''.join([str(s) for s in i]), 2), 'x') for i in table]]))] for i in range(1)]] for i in range(1)]

'''
# My thought process
input = 'AB+~AB+~A~B'
input = input.split('+')
print(input)

table = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0]
]
# Get pos w/ format of [row][col]
correspond = {
    'A': ['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][1]', '[1][1]', '[2][1]', '[3][1]'],
    'B': ['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[1][0]', '[1][1]', '[1][2]', '[1][3]'],
    'C': ['[0][1]', '[1][1]', '[2][1]', '[3][1]', '[0][2]', '[1][2]', '[2][2]', '[3][2]'],
    'D': ['[1][0]', '[1][1]', '[1][2]', '[1][3]', '[2][0]', '[2][1]', '[2][2]', '[2][3]'],
    '~A':['[0][2]', '[1][2]', '[2][2]', '[3][2]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],
    '~B':['[2][0]', '[2][1]', '[2][2]', '[2][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]'],
    '~C':['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],
    '~D':['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]']
}

a = ['a', 'b', 'c', 'd']
b = ['c', 'b', 'e', 'f']
c = ['b', 'f', 'a', 'k']

lists = [b,c]

print([i for i in [i for i in a for l in lists for x in l if i==x] if [i for i in a for l in lists for x in l if i==x].count(i)==len(lists)])

blah = [0]
# Exec it to covert, i just use table to get pos
exec('blah[0] = 1')


print([i.upper() if i.isalpha() else i for i in [format(int(''.join([str(s) for s in i]), 2), 'x') for i in table]])
'''
# Final thoughts: This works
'''
inputs = ['AB+~AB+~A~B',
'AB~C~D+AB~CD+~A~B~CD',
'AB~C~D+~AB~C~D+A~B~C~D',
'B~D+~B~D',
'~A~BD+~A~B~D',
'B~D+~A~BD+A~B~C',
'~B~C+BCD+B~C~D',
'A~C+ACD+~A~CD',
'AB~D+~ABD+A~BD+~A~B~D',
'B~D+~A~CD+~A~B~C~D']

for item in inputs:

    # I need this as editable... not sure how to do that without a semicoln :/
    table = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    # I can just loop this cause its j for refs
    correspond = {
        'A': ['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][1]', '[1][1]', '[2][1]', '[3][1]'],
        'B': ['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[1][0]', '[1][1]', '[1][2]', '[1][3]'],
        'C': ['[0][1]', '[1][1]', '[2][1]', '[3][1]', '[0][2]', '[1][2]', '[2][2]', '[3][2]'],
        'D': ['[1][0]', '[1][1]', '[1][2]', '[1][3]', '[2][0]', '[2][1]', '[2][2]', '[2][3]'],
        '~A':['[0][2]', '[1][2]', '[2][2]', '[3][2]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],
        '~B':['[2][0]', '[2][1]', '[2][2]', '[2][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]'],
        '~C':['[0][0]', '[1][0]', '[2][0]', '[3][0]', '[0][3]', '[1][3]', '[2][3]', '[3][3]'],
        '~D':['[0][0]', '[0][1]', '[0][2]', '[0][3]', '[3][0]', '[3][1]', '[3][2]', '[3][3]']
    }


    indivs = list(item.split('+'))
    for small in indivs:
        small = list(small)
        complexLen = [int(i) for i in ''.join([str(i)*(len(small)-i) for i in range(len(small))])]
        notStuff = [''.join([small.pop(i), small.pop(i)]) for i in complexLen if i < len(small) and small[i] == '~']
        lists = [correspond[i] for i in (notStuff+small)]

        somevar = [i for i in lists[0] for l in lists[1:] for x in l if i==x]

        for i in [i for i in somevar if somevar.count(i)==len(lists)-1]:
            exec('table'+i+'=1')

    print([i.upper() if i.isalpha() else i for i in [format(int(''.join([str(s) for s in i]), 2), 'x') for i in table]])
'''




