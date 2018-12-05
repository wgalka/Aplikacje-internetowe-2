class Transportation:
    wheels = 0

    def __init__(self):
        self.wheels = -1

    def travel_one(self):
        print("Travelling on generic transportation")

    def travel(self, distance):
        for _ in range(distance):
            self.travel_one()

    def is_auto(self):
        return self.wheels == 4

class Bike(Transportation):

    def travel_one(self):
        print("Biking one mile")

class Car(Transportation):
    wheels = 4

    def travel_one(self):
        print("Driving one mile")

    def make_sound(self):
        print("VROOM")

class Ferrari(Car):
    pass

t = Transportation()
b = Bike()
c = Car()
f = Ferrari()


isinstance(t, Transportation)

isinstance(b, Bike)
isinstance(b, Transportation)
isinstance(b, Car)
#isinstance(b, t) isinstance() arg 2 must be a type or tuple of types

isinstance(c, Car)
isinstance(c, Transportation)

isinstance(f, Ferrari)
isinstance(f, Car)
isinstance(f, Transportation)

issubclass(Bike, Transportation)
issubclass(Car, Transportation)
issubclass(Ferrari, Car)
issubclass(Ferrari, Transportation)
issubclass(Transportation, Transportation)

b.travel(5)
print(c.is_auto())
print(f.is_auto())
print(b.is_auto())
#b.make_sound()  'Bike' object has no attribute 'make_sound'
c.travel(10)
print("------------------------------")
f.travel(4)
