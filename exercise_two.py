class Venicle:
    def __init__(self, name: str,color: str, max_speed: int, seats: int ) -> None:
        self.seats = seats
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def get_color(self) -> str:
        return self.color
    
    def get_name(self) -> str:
        return self.name

    def get_seats(self) -> int:
        return self.seats

    def get_max_speed(self) -> int:
        return self.max_speed
    
    def get_fare(self):
        return self.seats * 100

class Bus(Venicle):
    def __init__(self) -> None:
        super().__init__(name = "Atlas", color = "blue", max_speed = 90, seats=50)

    def get_bus_fare(self):
        full_fare = super().get_fare()
        maintenance_charge = full_fare * 0.1
        return full_fare + maintenance_charge
        
    

class Taksi(Venicle):
    def __init__(self, meter_rate: int, distance: int) -> None:
        super().__init__(name = "Bolt", color = "red", max_speed = 110, seats=1)
        self.meter_rate = meter_rate
        self.distance = distance

    def get_taksi_fare(self) -> int:
        taksi_fare = super().get_fare()
        return taksi_fare * self.seats * self.meter_rate * self.distance


class Train(Venicle):
    def __init__(self,number_of_carts: int, passengers_number: int) -> None:
        super().__init__(name = "Fast", color = "white", max_speed = 220, seats=1)
        self.number_of_carts = number_of_carts
        self.passengers_number = passengers_number

    def get_train_fare(self):
        train_fare = super().get_fare()
        return train_fare * self.seats * self.number_of_carts * self.passengers_number


bus = Bus()
taksi = Taksi(meter_rate = 1, distance = 0.5)
train = Train(number_of_carts = 10, passengers_number = 20)
print(f"Bus price: {bus.get_bus_fare()}")
print(f"Name: {bus.get_name()}")
print(f"Color: {bus.get_color()}")
print(f"Seats: {bus.get_seats()}")
print(f"Max speed: {bus.get_max_speed()}")

print(f"Taksi price: {taksi.get_taksi_fare()}")
print(f"Train price: {train.get_train_fare()}")
