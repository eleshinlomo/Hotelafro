
"""
  This program will have different functions that will help hotel businesses.
  This program aims to automate most of recurring processes in hospitality businesses.
"""



print("HOTELAFRO SOFTWARE FOR HOSPITALITY BUSINESSES {}".format("(DEMO VERSION)"))

#The main class for this program starts here. All methods for this proposed software will be defined within this class.

#user input information for hotel guests
class Hotelafro:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender

#This method takes all inputs from the init above and summarize all guest details at once.
    def info(self):
        return "New Guest Created! NAME: {} {}, GENDER: {}".format(self.firstname, self.lastname, self.gender)


#This line is an instance of the class. Adds new guests as object to the Hotelafro class.
guest_1 = Hotelafro(input("Enter Firstname: "), input("Enter Lastname: "), input("Enter Gender: "))
print(guest_1.info())



















