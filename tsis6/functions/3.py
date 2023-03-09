def IsPalindrome(string):
    reverse=''.join(reversed(string))
    if string==reverse:
        return "YES"
    else:
        return "NO"
string="abbbba"
print(IsPalindrome(string))