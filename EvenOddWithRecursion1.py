def separate_even_odd(lst, even=[], odd=[]):
    if len(lst) == 0:          # Base condition
        return even, odd
    else:
        if lst[0] % 2 == 0:
            even.append(lst[0])
        else:
            odd.append(lst[0])

        return separate_even_odd(lst[1:], even, odd)


# User input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_list, odd_list = separate_even_odd(numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
