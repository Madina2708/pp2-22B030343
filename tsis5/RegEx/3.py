import re
my_str = input('Enter a string: ')
k = re.compile('[a-z]+_[a-z]+')
m = k.search(my_str)
if m:
    print('Found')
else:
    print('No match found')