class Shape():
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"{self.name} bu geometrik shakldir."


class Triangle(Shape):
    def info(self):
        super().__init__("Uchburchak")
    def sides(self):
        return 3

class Square(Shape):
    def info(self):
        super().__init__("To'rtburchak")
    def sides(self):
        return 4



x = Shape("Kvadrat")
print(Triangle("Uchburchak"))