# Amazing oneliner
for line in list(open('inputs.txt', 'r').readlines()): print(''.join([str(i)[-1] for i in [int(i)+int(line.split()[0][-int(line.split()[1])]) for i in line.split()[0][:-int(line.split()[1])]]+[int(line.split()[0][-int(line.split()[1])])]+[abs(int(i)-int(line.split()[0][-int(line.split()[1])])) for i in line.split()[0][-int(line.split()[1])+1:]]]))

'''
breakdown:
line = list(open('inputs.txt', 'r').readlines())
specialNumb = int(line.split()[0][-int(line.split()[1])])
first = [int(i)+specialNumb for i in line.split()[0][:-int(line.split()[1])]]
second = [abs(int(i)-specialNumb) for i in line.split()[0][-int(line.split()[1])+1:]]
print(''.join([str(i)[-1] for i in first+[specialNumb]+second]))

Honestly I should just be given like bonus points cause my program is so good...
'''
