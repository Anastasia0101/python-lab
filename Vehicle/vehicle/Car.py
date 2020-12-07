from .Direction import direction
from Vehicle.parts.CarGear import gear 
from Vehicle.parts.EnergySource import energySource 
from Vehicle.parts.Engine import engine


class Car(Vehicle):
    def __init__(self):
        super().__init__(energySource, engine, gear)

    def accelerate(self):
        print("car accelerated")
        super(Car, self).accelerate()

    def turn(self, direction):
        print("car");
        super(Car, self).turn(direction)

    def brake(self):
        super(Car, self).brake()
