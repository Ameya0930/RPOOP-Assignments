#polymorphism - poly(many) morph(forms)
#types of polymorphism
#Duck typing
#operator overloading
#Method overriding

class Vehicle():

    def __init__(self,name,number,colour,old):
        self.name = name
        self.number = number
        self.colour = colour
        self.old = old

    #operator overoading
    def __add__(self,other):        #overloading  the +operator, returns the age of whichever of the vehicle given in argument is older
        if(self.old>other.old):
            return self.old
        
        else:
            return other.old
        
    def rev(self):
        print("Sound")
    
    def DisplayProp(self):
        print("Name: ",self.name)
        print("Number: ",self.number)
        print("Colour: ",self.colour)
        print("Age: ",self.old)
    
class car(Vehicle):

    def rev(self):                  #Method overriding
        print("VROOOOM")
    
    
class Human():

    def __init__(self,name,number,colour,old):
        self.name = name
        self.number = number
        self.colour = colour            #skintone
        self.old = old                  #age


v1 = Vehicle("activa",3529,"while",4)
c1 = car("Verna",4257,"brown",3)

h1 = Human("Yash",123456789,"brown",19)


v1.rev()
c1.rev()    #car is a subclass to vehicle, the class car has a rev function which overrides the already present rev function in the parent class vehicle
 
c1.DisplayProp()
#Duck typing
Vehicle.DisplayProp(h1)     #an objet of type human is not the same as object of type vehicle
                            #class human didnt have the method display prop
                            #still it wors fine as both objects have same properties/instance variables