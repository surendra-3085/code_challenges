import re
password = input("enter the passward")
userid = re.match('^[a-z]{3}[0-9]{3}',password)
if userid:
    print("valid password")
else:
    print("invalid password")

                  
