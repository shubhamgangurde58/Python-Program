def find_fact(num):

    fact = 1
    i = 1

    while (i <= num):
        fact *= i
        i += 1
    return fact

# main function 
num = int(input("Enter the any number : "))
result = find_fact(num)
print(num," Factorial = ",result)