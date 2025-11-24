percentage = int(input("Enter the Percentage  : "))

if(percentage >= 90 and percentage <= 100):
    print(" Congratulation Pass With A+ grade !")
elif(percentage >= 70 and percentage < 90):
    print(" congratulation Pass with B+ grade !")
elif(percentage >= 50 and percentage < 70):
    print(" Congratulation Pass With C+ grade !")
else:
    print("Sorry ! You Are Fail ! ")