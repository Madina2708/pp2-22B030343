def squares(n):
    for i in range(n+1):
        yield i**2 

for i in squares(int(input())):
    print(i, end=" ")