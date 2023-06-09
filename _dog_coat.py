class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")    

    def get_info(self):
        print(f"Dog Coat Color: {self.coat_color}")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)       

    def jump(self):
        print(f"{self.name} is jumping!")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)            

    def sit(self):
        print(f"{self.name} has Sitted Down!")

# Creating Objects and implementing its functionalities
dog1 = Dog("Bruno", 2, "white")
dog1.description()
dog1.get_info()
print()            

dog2 = JackRussellTerrier("Charlie", 4, "Black")
dog2.description()
dog2.get_info()
dog2.jump()
print()

dog3 = Bulldog("Rocket", 4, "Brindle")
dog3.description()
dog3.get_info()
dog3.sit()
print()