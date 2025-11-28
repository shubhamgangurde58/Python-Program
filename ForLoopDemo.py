

# for i in range(1,10):
#     print(i)


# for i in range(2,50,2):
#     print(i)

# num = int(input("Enter the value of n : "))
# sum = 0
# for i in range(num):
#     sum += i

# print("sum := ",sum)

# # Question 4

# num = int(input("Enter the any number to print the table : "))
# for i in range(10+1):
#     print(num ," x ", i," = " ,i*num) 


 # Question 5 

mystr = input("Enter the any String : ")
vowels = "aeiouAEIOU"
count = 0

for ch in mystr:
    if ch in vowels:
        count += 1

print(count)