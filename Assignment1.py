class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def rectangle_area(self):
        return self.length * self.width


    def rectangle_perimeter(self):
        return (self.length + self.width)*2


    def changeDimension(self):
        self.length = eval(int(input("Enter the length of the rectangle:\n")))
        self.width = eval(int(input("Enter the width of the rectangle:\n")))

a = Rectangle(2,3)

print(a.rectangle_area())
print(a.rectangle_perimeter())

