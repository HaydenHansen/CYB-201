# starting to work with classes and subclasses
#Parent class is Vehicle
class Vehicle():
    def description(self):
        print("I'm a", self.color, "Vehicle")

# Car is a subclass of Behicle
class Car(Vehicle):
    def setDescription(self, speed, color):
        print("I am a", color,"car now travling at", speed,"miles per hour")
    
#motorcycle is a subclass of Vehicle
class Moto(Vehicle):
    def setDescription(self, speed, color):
        print("I am a", color, "motorcycle and I just passed you at", speed,"Miles per hour")

class formula1(Vehicle):
    def setDescription(self, speed, color):
        print("I am a",color,"formula1 car and I beat you all at", speed, "miles per hour")

class Bike(Vehicle):
    def setDescription(self, speed, color):
        print("I am a", color, "bike and I cant keep up, im only going", speed,"miles per hour")
    


#create an object from each class
v = Vehicle()
c = Car()
m = Moto()
f = formula1()
b = Bike()

#set descriptions
c.setDescription(25,"green")
m.setDescription(55,"black")
f.setDescription(190,"purple")
b.setDescription(10,"red")


#anything below this line is irrelevent and was lines that didnt work
#set Colors
#c.setColor("Green")


# Prints now traveling at 25 miles per hour
#v.setSpeed(25)
# Triggers AttributeError: 'Vehicle' onject has no attribute 'setSpeed'
