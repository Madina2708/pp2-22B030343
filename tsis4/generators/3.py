def gen(m):
    global count 
    count = 0
    for i in range(m+1):
        if i%3 == 0 and i%4==0: 
            count=count + 1
            yield i
                  

m= int(input())
for i in gen(m):

    if count != 0:
        count-=1
        print(i, end =" ")
   