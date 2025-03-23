fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

many = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        many[w] = many.get(w,0) + 1

# find the top 5 word by frequency

print(many)
print (sorted(many))