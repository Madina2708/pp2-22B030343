import re
string = 'CamelCaseName'
string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
print(string) 