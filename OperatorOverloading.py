class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

# main 
a = Number(10)
b = Number(20)

print(a+b)