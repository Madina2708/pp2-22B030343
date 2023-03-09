def mult(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(mult((5, 2, 4, -1, 7)))