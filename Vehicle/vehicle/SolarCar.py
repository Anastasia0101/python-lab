from Vehicle.parts.CarGear import CarGear
from Vehicle.parts.Gear import Gear
from Vehicle.parts.EnergySource import EnergySource
from Vehicle.parts.Engine import Engine
from Vehicle.parts.SolarBattery import SolarBattery
from Vehicle.parts.SolarEngine import SolarEngine


class SolarCar(Car): 

    def __init__(self, capacityBattery):
        super().__init__(SolarBattery(capacityBattery), SolarEngine(), CarGear())

    def accelerate(self):
        print("Solar car is accelerated")
        super(SolarCar, self).accelerate()

    def turn(self, direction):
        print("Solar car");
        super(SolarCar, self).turn(direction)

    def brake(self):
        super(SolarCar, self).brake()
