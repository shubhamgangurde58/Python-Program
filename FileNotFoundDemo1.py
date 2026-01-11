try :
    file = open("data.txt","r")
    print(file.read())
    file.close()

except FileNotFoundError as e:

    print("File not Found Error !" , e)

