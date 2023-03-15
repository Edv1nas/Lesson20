class Vehicle:
    def __init__(self, name: str) -> None:
        self.name: str = name

def get_name(self) -> str:
    return self.name

class Engine:
    def __init__(self) -> None:
        pass

    def say_hi_engine(self) -> None:
        print("Hi engine")

class Golf(Vehicle, Engine):
    def __init__(self, name: str, cost: float) -> None:
        super().__init__(name=name)
        Engine.__init__(self, name=name)
        self.cost: float = cost

    def get_cost(self) -> float:
        return self.cost
    

CAR_NAME = "Good car"   
my_car = Golf(name=CAR_NAME, cost=100)

print(my_car.say_hi_engine())
