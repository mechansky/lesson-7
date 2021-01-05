from abc import ABC, abstractmethod


class Clothes(ABC):
    total_consumption = 0
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        consumption = ((self.size/6.5) + 0.5)
        Clothes.total_consumption += consumption
        return f'расход ткани на товар {self.name} составляет {round(consumption, 2)}'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        consumption = (self.height*2) + 0.3
        Clothes.total_consumption += consumption
        return f'расход ткани на товар {self.name} составляет {round(consumption, 2)}'


product_1 = Suit('Костюм HENDERSON', 170)
print(product_1.consumption)

product_2 = Coat('Пальто GUCCI', 48)
print(product_2.consumption)

print(f'полный расход ткани составляет: {round(Clothes.total_consumption, 2)} ')




