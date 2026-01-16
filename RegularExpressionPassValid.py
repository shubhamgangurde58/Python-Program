# Program to check password validity using regular expression 

import re 

password = input("Enter Password : ")

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$]).{6,}$'

if re.match(pattern , password):
    print("Valid Password")
else:
    print("Invalid Password")

    