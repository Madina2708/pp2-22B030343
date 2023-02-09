def check__Palindrome(str):
	left_pos = 0
	
	right_pos = len(str) - 1
	
	while right_pos >= left_pos:
		if not str[left_pos] == str[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True

print(check__Palindrome('madam')) 
print(check__Palindrome('mom')) 
print(check__Palindrome('cinnamon')) 