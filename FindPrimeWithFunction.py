# Write a function that takes a list of numbers and returns a new list containing only the prime numbers.

def check_prime(num):

    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if(num % i == 0):
                return False
        return True

# main function 
list1 = [5,7,10,50,6,4,3,9,11]
prime_list = []

for i in list1:
    if(check_prime(i)):
        prime_list.append(i)

print("Prime List =",prime_list)
    