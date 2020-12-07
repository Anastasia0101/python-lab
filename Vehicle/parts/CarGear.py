from Vehicle.Force import Force

class CarGear(Gear):

    def consume(self, Force):
        print("start motion")
        super(CarGear, self).consume(Force)