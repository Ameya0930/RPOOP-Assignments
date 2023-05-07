import math
class Polygon():
    def __init__(self,side,length):
        self.side = side
        self.length = length

    def polygon_area(self):
        return[(self.length)**2*self.side/(4*math.tan(math.pi/self.side))]

    def polygon_perimeter(self):
        return (self.side*self.length)

    def changeDimension(self):
            self.side= eval(int(input("Enter the number of sides of a polygon:\n")))
            self.length = eval(int(input("Enter the length of the polygon:\n")))

class square(Polygon):
        def __init__(self,length):
            self.length= length
            self.side =4

a =Polygon(4,2)
sq= square(5)

print(a.polygon_area())
print(a.polygon_perimeter())
print(sq.polygon_area())