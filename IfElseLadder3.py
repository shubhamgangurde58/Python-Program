A = int(input("A : "))
B = input("M/F : ")

if( A == 1 or A == 2 and  B == 'M'):
    print("fee is 100")
elif(A == 3 or A == 4 and B == 'F'):
    print("fee is 200")
elif(A == 5 and B == 'M'):
    print("fee is 300")
else:
    print("No Fee !")