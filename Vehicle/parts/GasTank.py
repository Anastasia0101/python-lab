from Vehicle.Energy import Energy
from Vehicle.parts.EnergySource import EnergySource

class GasTank(EnergySource):

    def __init__(self, capacity):
        self.__capacity = capacity

    def get(self, Energy):
        energy = round(self.capacity * 2)
        super(GasTank, self).get()
        return Energy(energy)
        