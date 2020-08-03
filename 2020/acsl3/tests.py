a = ['a', 'b', 'c', 'd']
b = ['c', 'b', 'e', 'f']
c = ['b', 'f', 'a', 'k']

lists = [b,c]

print([i for i in [i for i in a for l in lists for x in l if i==x] if [i for i in a for l in lists for x in l if i==x].count(i)==len(lists)])
