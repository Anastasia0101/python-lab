from Vehicle.Force import Force
from .Gear import Gear 

class BoatGear :
    def __init__(self):
        self.gear = Gear()

    def consume(self, Force):
        print("start motion")
