
def show(n):
    sum = 0
    if(n == 0):
        return 0
    return show(n-1) + n

        

n = int(input("Enter the value of N : "))
print("Sum = ",show(n))