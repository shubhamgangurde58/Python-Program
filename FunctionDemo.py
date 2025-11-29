# def calc_sum(a,b):
#     return a+b

# a = int(input("Enter the Value of A : "))
# b = int(input("Enter the Value of B : "))
# print(calc_sum(a,b))

# def list_length(mylist):
#     return len(mylist)

# mylist = [10,20,30,30]
# print(list_length(mylist))

# def find_factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# n = int(input("Enter the Value of N : "))
# print(find_factorial(n))


# def calc_INR(USD):
#     INR = USD * 83
#     return INR

# USD = int(input("Enter the USD : "))
# INR = calc_INR(USD)
# print(USD , "USD = ",INR,"INR")

def find_evenORodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter the any Number : "))
mystr = find_evenORodd(num)
print(mystr)