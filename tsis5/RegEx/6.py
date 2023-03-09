import re
text = 'The memory warms you up inside, but it also breaks your soul apart'
print(re.sub("[ ,.]", ":", text))