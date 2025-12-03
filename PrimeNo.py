def check_prime(n):
    i = 2
    while(i != n):
        if(n % i == 0):
            return "Number is Not Prime !"
        i = i + 1
    return "Number is Prime !"
    

# main function 
n = int(input("Enter the any number : "))
str1 = check_prime(n)
print(str1)