from Vehicle.Force import Force
from Vehicle.Energy import energy

class SolarEngine(Engine):

    def transform(self, energy):
        return Force(energy.getAmount())