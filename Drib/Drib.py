class Drib: 

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def sum(self, n, d):
        return n + d

    def get_subtraction(self, n, d): 
        return d - n
    
    def get_multiplication(self, n, d): 
        return n * d
    
    def get_division(self, n, d):
        return d / n

    def pow(self, n, d):
        return d**n

num = int(input('Input numerator: '))
den = int(input('Input denominator: '))

d = Drib(num, den)

print (f'Your drib: {d.numerator} / {d.denominator}')
print (f'Sum: {d.sum(d.numerator, d.denominator)}')
print (f'{d.denominator} - {d.numerator }: {d.get_subtraction(d.numerator, d.denominator)}')
print (f'{d.denominator} * {d.numerator }: {d.get_multiplication(d.numerator, d.denominator)}')
print (f'{d.denominator} / {d.numerator }: {d.get_division(d.numerator, d.denominator)}')
print (f'{d.denominator} ** {d.numerator }: {d.pow(d.numerator, d.denominator)}')

