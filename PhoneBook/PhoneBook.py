import json

class Contact: 

    def __init__(self, name, surname, middle_name, phone, add_info):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name 
        self.phone = phone
        self.add_info = add_info

    @classmethod
    def two_param(self, name, phone):
        self.name = name 
        self.phone = phone

    @classmethod
    def three_param(self, name, phone, add_info):
        self.name = name
        self.phone = phone 
        self.add_info = add_info

    def show_info(self):
        print("Name: " + self.name)
        print("Surname: " + self.surname)
        print("Middlename: " + self.middle_name)
        print("Phone: " + self.phone)
        print("Additional information: " + self.add_info)

    def show_json_info(self):
        contacts = {
            'Name': self.name,
            'Surname' : self.surname,
            'Middlename' : self.middle_name,
            'Phone' : self.phone,
            'Addition information' : self.add_info
        }
        return contacts

    def __del__(self):
        print("Contact is deleted")

class PhoneBook( Contact ):

    def __init__(self):
        print("init")

    def __del__(self):
        print("Contact is from phonebook deleted")

    name = input("Input name: ")
    surname = input("Input surname:")
    middle_name = input("Input middle name:")
    phone = input("Input number of phone: ")
    add_info = input("Input additional information: ")

    contact = Contact(name, surname, middle_name, phone, add_info)
    contact.show_info()

    info_json = json.dumps(contact.show_json_info())
    print(info_json)
   
