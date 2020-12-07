class Vehicle:

    def __init__(self, engine, wheels, gas_tank):
        self.engine = engine
        self.wheels = wheels
        self.gas_tank = gas_tank

    def __accelerate(self):
        print('Accelerate')
