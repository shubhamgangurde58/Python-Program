# create a library class and compute fine 

class library:
    
    def __init__(self, acc_no , title , author , days):

        self.acc_no  = acc_no
        self.title = title
        self.author = author
        self.days = days

    def fine(self):
        return self.days * 5

    def display(self):
        print("Acc No : ",self.acc_no)
        print("Title : ",self.title)
        print("Author : ",self.author)
        print("Fine : ",self.fine())


# main 
acc = input("Enter the Acc Number : ")
title = input("Enter the Title : ")
author = input("Enter the Author : ")
days = input("Enter the late days ")

b = library(acc,title,author,days)
b.display()