from Vehicle.parts.BoatGear import BoatGear
from Vehicle.parts.GasTank import GasTank
from Vehicle.parts.GasolineEngine import GasolineEngine
from Vehicle.vehicle.Boat import Boat
from Vehicle.vehicle.Car import Car
from Vehicle.vehicle.Driveable import driveable
from Vehicle.vehicle.SolarCar import SolarCar
from Vehicle.vehicle.Vehicle import Vehicle
from Vehicle.parts.CarGear import CarGear
from Vehicle.parts.SolarBattery import SolarBattery
from Vehicle.parts.SolarEngine import SolarEngine
from Vehicle.vehicle.Direction import Direction

class Main:
    boat = Boat(GasTank(50), GasolineEngine(), BoatGear())
    car = Car(GasTank(50), GasolineEngine(), CarGear())
    solarCar = SolarCar(50)

    vehicles = [boat, car, solarCar]
    index = 0
    for index in range(len(vehicles)):
        testDrive(vehicles[index])

    def testDrive(self, driveable):
        driveable.accelerate()
        driveable.turn(Direction.LEFT)
        driveable.turn(Direction.RIGHT)
        driveable.brake()
        driveable.accelerate()
        driveable.brake()