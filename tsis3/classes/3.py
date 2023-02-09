class Rectangle():
    def __init__(self,q,r):
        self.length = q
        self.width = r

    def area(self):
        return self.length*self.width


rect = Rectangle(11,9)

print(rect.area())