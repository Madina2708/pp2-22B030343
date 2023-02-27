import re

def match(text):
        patterns = 'ab{2,3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return ('Not matched!')

print(match("abb"))
print(match("aabbbbbc"))
print (match("abbb"))
print (match("ab"))
print(match("abbbbbbbbbbb"))
print (match("fffbbb"))