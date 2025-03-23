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

largest = None
bigword = None
for cle, valeur in many.items() :
    if largest is None or valeur > largest :
        largest = valeur
        bigword = cle

print(bigword,largest)