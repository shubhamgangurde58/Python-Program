# Write a recursive function to calculate the sum of all elements in a list.

def list_sum(list1):
    if(len(list1) == 0):
        return 0
    else:
       return list1[0] +  list_sum(list1[1:])

# main function 
list1 = [10,20,30,40,50]
result = list_sum(list1)
print("Sum of List = ",result)
