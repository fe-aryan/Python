class car:
    wheels=4
    #static variable- used by entire class
    #Instance variables -  value varies from obj to obj
    def _init_(self):
           self.company= "BMW"
           self.mileage=10

car1 = car()
car2 = car()
car.wheels=5#static variable class ke through change hota hai

print(car1.mileage,car1.wheels)
print(car2.mileage,car2.wheels)