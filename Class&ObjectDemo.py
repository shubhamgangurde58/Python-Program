class Student:
    def __init__(self):
        print("Object Created Successfully !!")
    
    def set_data(self, id, name , fees):
        self.id = id
        self.name = name 
        self.fees = fees

    def get_data(self):
        print("id : = ",self.id)
        print("name : =",self.name)
        print("Fees : = ",self.fees)
        print("------------------")

# main function
s1 = Student()
s1.set_data(101,"shubham",50000)
s1.get_data()

s2 = Student()
s2.set_data(102,"jayesh",60000)
s2.get_data()
