
def add_recursive(a, b):
    if b == 0:
        return a
    else:
        return add_recursive(a + 1, b - 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_recursive(num1, num2)

print("Addition is:", result)
