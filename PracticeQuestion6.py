# Check the give number is even or Odd 

num = int(input("Enter any number : "))

if(num % 2 == 0):
    print("Number is even :")
else:
    print("Number is Odd :")
    print("\n\n")

# Take a  Three number as input check which one is greater 

a = int(input("Enter the Value of A : "))
b = int(input("Enter the Value of B : "))
c = int(input("Enter the Value of C : "))

if(a > b ):
    if(a > c ):
        print(" A is Big ")
    else:
        print(" C is Big ")
else:
    if(b > c):
        print(" B is Big ")
    else:
        print(" C is Big ")

# check the number is multiple by 7 of not 

num2 = int(input("Enter any Number "))

if(num2 % 7 == 0):
    print(" True Give number is Multiple by 7 ",num2)
else:
    print("False give number is not Multiple by 7 ",num2)