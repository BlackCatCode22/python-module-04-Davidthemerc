han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:',line)
    wds = line.split()
    #print('Words:',wds)
    # Guardian Pattern (stronger)
    if len(wds) < 3 :
        continue
    # Potentially faulty code (without guardian pattern)
    if wds[0] != 'From' :
        #print('Ignore')
        continue
    print (wds[2])