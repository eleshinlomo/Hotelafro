
"""
  This program will have different functions that will help hotel businesses.
  This program aims to automate most of recurring processes in hospitality businesses.
"""

#The main class for this program starts here. All methods for this proposed software will be defined within this class.

class hotelSolution:
    def __init__(self):
        psssssss
#Here is the first method that only takes info about guests.

def guestInfo():
    guest_firstname= str(input("What is your First Name: "))
    guest_lastname = str(input("What is your Last Name: "))
    num_days = int(input("Please enter number of days guest will stay: "))

    return "Here is the info you entered: NAME: {} {} NUMBER OF NIGHTS: {}".format(guest_firstname, guest_lastname, num_days)

info = guestInfo()

print(info)







