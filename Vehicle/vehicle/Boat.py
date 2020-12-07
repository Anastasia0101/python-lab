from Vehicle.parts.BoatGear import gear
from Vehicle.parts.EnergySource import energySource
from Vehicle.parts.Engine import engine

class Boat(Vehicle):

    def __init__(self):
        super().__init__(energySource, engine, gear)

    def accelerate(self):
        print("Boat accelerated")
        super(Boat, self).accelerate()

    def turn(self, direction):
        print("Boat");
        super(Boat, self).turn(direction)

    def brake(self):
        super(Boat, self).brake()
