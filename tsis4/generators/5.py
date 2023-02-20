def gen(N):
    for i in range(N,0, -1):
        yield i

for i in gen(input()):
     print(i)