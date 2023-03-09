import re
string='HelloWorld' 
wspaces = re.findall('[A-Z][a-z]*', string)

print(' '.join((wspaces)))