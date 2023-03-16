"""Task Nr.3

Define the Animal, Mammal, and Primate classes.
Animal should have a name attribute and a make_noise() method.
Mammal should have a warm_blooded attribute and a give_birth() method.
Primate should have an opposable_thumbs attribute and a swing() method.
Test the classes by creating a Chimpanzee and making it do various things :) 🐒"""

class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def make_noise(self):
        return(f"{self.name} makes funny noises all the time.")

class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        super().__init__(name)
        self.warm_blooded: bool = warm_blooded

    def give_birth(self):
        return(f"{self.name} can't give birth, because he is a man :D")

class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: str) -> None:
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs

    def swing(self):
        return(f"{self.name} likes to swing on tree branches")

chimpanzee = Primate("Kebas", "True", "True")
print(chimpanzee.name)
print(chimpanzee.warm_blooded)
print(chimpanzee.opposable_thumbs)
print(chimpanzee.make_noise())
print(chimpanzee.give_birth())
print(chimpanzee.swing())