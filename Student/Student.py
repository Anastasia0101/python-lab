class Student( object ):

    def __init__(self, name, age, sex, phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone

    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self, age):
        return self.age

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self, sex):
        return self.sex

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self, phone):
        return self.phone

    def show_info(self):
        print("Name: " + self.name)
        print(f'Age: {self.age}')
        print("Sex: " + self.sex)
        print(f'Phone: {self.phone}')

    def show_format_info(self):
        print(self.name.center(40, ' '))
        print(str(self.age).center(40, ' '))
        print(self.sex.center(40, ' '))
        print(str(self.phone).center(40, ' '))

class Main( Student ):

    def __init__(self):
        print("Init")

    name = input("Input name: ")
    age = int(input("Input age:"))
    sex = input("Input sex:")
    phone = int(input("Input number of phone: "))

    s = Student(name, age, sex, phone)
    s.show_info()

    str = "Some words"
    s.show_format_info()