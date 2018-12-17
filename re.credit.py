import re
credit_number = input("enter card number")
cardnumber = re.match('^[0-9]{4}[a-z]{4}',credit_number)
if cardnumber:
    print("valid number")
else:
    print("invalid number")

      
