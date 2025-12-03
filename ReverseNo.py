def print_reverse(num):
    reverse = 0
    reminder = 0

    while(num != 0):
        reminder = num % 10
        reverse =  (reverse * 10) + reminder
        num = num // 10
    return reverse

# main function 
num = int(input("Enter the any 3 digit number : "))
result = print_reverse(num)
print(result)