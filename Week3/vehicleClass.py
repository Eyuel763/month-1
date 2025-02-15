class Vehicle:
    def __init__(self, make, model, num_wheels):
        self.make = make
        self.model = model
        self.num_wheels = num_wheels

    def __str__(self):
        return f"{self.make} {self.model} ({self.num_wheels} wheels)"
    
    def describe(self):
        return f"This is a {self.make} {self.model} ({self.num_wheels} wheels)"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model, 4)
        self.num_doors = num_doors

    def __str__(self): 
        return f"{super().__str__()} ({self.num_doors} doors)"

    def describe(self):
        return f"This is a {self.make} {self.model} with {self.num_wheels} wheels and {self.num_doors} doors."

class Bike(Vehicle):
    def __init__(self, make, model, has_basket):
        super().__init__(make, model, 2)
        self.has_basket = has_basket

    def __str__(self):  
        return f"{super().__str__()} (Basket: {self.has_basket})"
        