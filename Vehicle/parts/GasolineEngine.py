from Vehicle.Energy import Energy
from Vehicle.Force import Force

class GasolineEngine(Engine):

    def transform(self, energy):
        return Force(energy.getAmount())
    