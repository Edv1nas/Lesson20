class Venicle:
    def __init__(self, seats: int ) -> None:
        self.seats = seats

    def get_color(self):
        return self.color
    
    def get_name(self):
        return self.name
    
    def get_fare(self):
        return self.seats * 100

class Bus(Venicle):
    def __init__(self) -> None:
        super().__init__(seats=20)

    def get_fare(self):
        full_fare = super().get_fare()
        maintenance_charge = full_fare * 0.1
        return full_fare + maintenance_charge
        
    

class Taksi(Venicle):
    def __init__(self, meter_rate: int, distance: int) -> None:
        super().__init__(seats=2)
        self.meter_rate = meter_rate
        self.distance = distance

    def get_taksi_fare(self) -> int:
        taksi_fare = super().get_fare()
        return taksi_fare * self.seats * self.meter_rate * self.distance


class Train(Venicle):
    def __init__(self,number_of_carts: int, passengers_number: int) -> None:
        super().__init__(seats=20)
        self.number_of_carts = number_of_carts
        self.passengers_number = passengers_number

    def get_train_fare(self):
        train_fare = super().get_fare()
        return train_fare * self.seats * self.number_of_carts * self.passengers_number


bus = Bus()
taksi = Taksi(meter_rate = 1, distance = 0.5)
train = Train(number_of_carts = 10, passengers_number = 2)
print(f" Bus: {bus.get_fare()}")
print(f" Taksi: {taksi.get_fare()}")
print(f" Train: {train.get_fare()}")

# taxi = Taksi(2, 0.5, 5)
# print(taxi.get_fare())
