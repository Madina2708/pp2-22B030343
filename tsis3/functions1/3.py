heads = 31 
legs = 96

def solve(t,l):
      if (l>t) and (legs%2==0):
        rabbit = (l-2*t)//2
        chick = t-rabbit
        print(f' There are {rabbit} Rabbits and {chick} chickens.')  
        
solve(heads, legs)