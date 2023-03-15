class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def area(self) ->int:
        pass
    
class Rectangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        super().__init__(name=Rectangle, sides=4)
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self,side_length: float) -> None:
        super().__init__(side_length, side_length)
        self.side_length = side_length

square = Square(4)
print(square.area())

