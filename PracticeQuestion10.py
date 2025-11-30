# with open("practice.txt","r") as f :
#   data =  f.read()
#   print(data)

#   new_data = data.replace("java","python")

#   with open("practice.txt","w") as f :
#     f.write(new_data)


# word = "learning"
# with open("practice.txt","r") as f :
#     data = f.read()
#     print(data)

#     if(data.find(word) != -1):
#         print("Found ")
#     else:
#         print("Not Found !")


# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1

#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1


# print(check_for_line())

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    print(nums)

    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)