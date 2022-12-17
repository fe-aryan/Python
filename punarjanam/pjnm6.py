class Car:
    pass

#write the code to create a child class bus that will inherit all the variables and methods of the vehicle class

class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def honk(self):
        print("Honk honk!")

class Bus(Vehicle):
    def __init__(self, make, model, year, color, capacity):
        super().__init__(make, model, year, color)
        self.capacity = capacity

    def pick_up_passengers(self, num_passengers):
        self.capacity -= num_passengers
        print(f"Picked up {num_passengers} passengers. {self.capacity} seats remaining.")

# Example usage
bus = Bus("Ford", "E350", 2020, "blue", 40)
bus.honk() # prints "Honk honk!"
bus.pick_up_passengers(5) # prints "Picked up 5 passengers. 35 seats remaining."
