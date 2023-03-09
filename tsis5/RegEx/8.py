import re
text = "TheMemoryWarmsYouUpInside,ButItAlsoBreaksYourSoulApart"
print(re.findall('[A-Z][^A-Z]*', text))