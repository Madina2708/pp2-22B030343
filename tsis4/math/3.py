import math
global pi 
pi=math.pi
def area_pol(s,n):
    angle=float(pi/n)
    apothem=float(s/(2*math.tan(angle)))
    area=int((apothem*s*n)/2)
    print(area)
s = float(input('Number of sides: '))
n=float(input('The length of a side: '))

print('The area of the polygon is: ', end="")
area_pol(n,s)