def has_33(num):
    for i in range(0, len(num)-1):
        if num[i:i+2] == [3,3]:
            return True
    return False

print(has_33([1, 3, 3]))