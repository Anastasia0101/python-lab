class Overcoat:

    color = ""
    price = 0
    season = ""
    size = 0

    def __init__(self, color, price, season, size):
        self.color = color
        self.price = price
        self.season = season
        self.size = size
    
    def __eq__(self, other):
        return 'Is equal? : {}'.format(self.color == other.color and self.price == other.price and self.season == other.season and self.size == other.size)

    def __gt__(self, other):
        return 'First is more expensive {}'.format(self.price > other.price)

    def __str__(self):
        return 'str Overcoat({}, {}, {}, {})'.format(self.color, self.price, self.season, self.size)

print("Input first overcoat: ")
color = input("Enter color: ")
season = input("Enter season: ")
price = int(input("Enter price: "))
size = int(input("Enter size: "))

overcoat_first = Overcoat(color, price, season, size)

print("Input second overcoat: ")
color = input("Enter color: ")
season = input("Enter season: ")
price = int(input("Enter price: "))
size = int(input("Enter size: "))

overcoat_second = Overcoat(color, price, season, size)

print(overcoat_first.__gt__(overcoat_second)) 
print(overcoat_first.__eq__(overcoat_second))
print(overcoat_first.__str__())
print(overcoat_second.__str__())
overcoat_first = overcoat_second
print(overcoat_first)