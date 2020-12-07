from Vehicle.Energy import Energy

class SolarBattery(EnergySource): 

    def __init__(self, capacity):
        self.__capacity = capacity

    def get(self, Energy):
        energy = round(self.capacity * 2)
        super(SolarBattery, self).get()
        return Energy(energy * 3)
        
