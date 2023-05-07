#types of inheritance
#Single inheritance
#Multiple Inheritance
#Multilevel inheritance
#Hierarchial inheritance
#Multipath inheritance

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
    
class car(Vehicle):                 #subclass car inherits from a single parent class (Single inheritance )
                                    #  Vehicle
                                    #     |
                                    #    car
    def rev(self):                  #Method overriding
        print("VROOOOM")
    
class EVcar(car):                   #evcar class is a subclass of class car, and class car is a subclass of class vehicle
    pass                            #(Multilevel inheritance)


class ICcar(car):                   #child class of the class car
    pass                            #Both evcar and ICcar are child classes of the class car
                                    #both inherit from single parent class
                                    #(Hierarchial inheritance)
                                    #      ------car-------
                                    #     |                |
                                    #  EVcar              ICcar
    
class Hybrid(EVcar,ICcar):          #Inheriting from two classes (Multiple inheritance)
    pass                            #also an example for (Multipath inheritance), inheriting from class car via two different paths
                                    #      ------car-------
                                    #     |       |        |
                                    #  EVcar      |       ICcar
                                    #     |       |        |
                                    #      ---- Hybrid----- 


