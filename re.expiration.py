import re
expiration_date = input("enter the date of credit card")
creditcard = re.match('^(([1-9])|(1[0-2]))\/(([0-9])|(1{0-9})|(2[0-2]))$',expiration_date)
if creditcard:
    print("card is valid")
else:
    print("card is expire")



                    
