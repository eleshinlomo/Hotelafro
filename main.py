
"""
  This program will have different functions that will help hotel businesses.
  This program aims to automate most of recurring processes in hospitality businesses.
"""

#The main class for this program starts here. All methods for this proposed software will be defined within this class.

class Hotelafro:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender

    def info(self):
        return "New Guest Created! NAME: {} {}, GENDER: {}".format(self.firstname, self.lastname, self.gender)

guest_1 = Hotelafro(input("Enter Firstname: "), input("Enter Lastname: "), input("Enter Gender: "))
print(guest_1.info())



















