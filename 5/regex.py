import re
lin = 'From stephen.marquad@uct.ac.za Sat Jan  5 09:14:16 20008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)