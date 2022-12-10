# class Laptop:

#     def _init_(self):
#         print("Hello World")
    
#     def config(self):
#         print("Asus","i7","1TB")

# laptop1=Laptop()
# laptop2=Laptop()
# #Laptop.config(laptop1)
# laptop1.config()
# laptop2.config()


# class student:

#     def info(self):
#         print("name","class")

# student1=student()#object
# student2=student()
# student1.info()


# init method is called by its own,called automatically
#
# class student:
#     def _init_(self,name,rollno):
#         self.name = name
#         self.rollno = rollno                              

#     def info (self):
        
#          print("name is : ", self.name,",roll no. is : ",self.rollno)

# student1=student("Shivani","65")#object
# student2=student("Upasana","66")

# print(id(student1))#(heap memory) location 
# print(id(student2))
# student1.info()
# student2.info()


# class person:
#     def _init_(self):
#         self.name = "Iram"
#         self.number = 30
# p1=person()
# p2=person()

# p1.name="kiram"

# print(p1.name)
# print(p2.name)



class person:
    def _init_(self):
        self.name = "Iram"
        self.number = 30

    def compare(self,other):
        if(self.number == other.number):
             return True
        else:
            return False
p1=person()
p2=person()#object
p2.number=18

if p1.compare(p2):
    print("SAME")
else:
    print("DIFFERENT")


print(p1.number)
print(p2.number)