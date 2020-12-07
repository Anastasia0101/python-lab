from Vehicle.vehicle.Vehicle import Vehicle
from Vehicle.vehicle.Direction import direction

class Driveable(InformalParserInterface):

    def accelerate(self):
        return self

    def turn(self, direction):
        return direction

    def brake(self):
        return self