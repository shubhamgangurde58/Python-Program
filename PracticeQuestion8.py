# Write a program that Takes a number as input Checks if the number is Positive Negative Zero Print the result.

num = int(input("Enter the any number : "))

if (num > 0):
    print(num," is Positive Number : ")
elif(num < 0):
    print(num," is Negative Number : ")
elif(num == 0):
    print(num, "is Zero :")
else:
    print("Invalid input !!")