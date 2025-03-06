han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:',line)
    if line == '' :
        print('Skip Blank')
        continue
    wds = line.split()
    print('Words:',wds)
    # Potentially faulty code (without guardian pattern)
    if wds[0] != 'From' :
        print('Ignore')
        continue
    print (wds[2])

    # Blowing up because of a blank line?