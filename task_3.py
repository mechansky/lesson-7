class Cell:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other):
        result = self.amount + other.amount
        return f'Количество клеток после объединения: {result}'

    def __sub__(self, other):
        result = self.amount - other.amount
        if result > 0:
            return f'Количество клеток после вычитания: {result}'
        else:
            print('количество клеток менее нуля!')

    def __mul__(self, other):
        result = self.amount * other.amount
        return f'Количество клеток после умножения: {result}'

    def __truediv__(self, other):
        result = round(self.amount / other.amount)
        return f'Количество клеток после деления: {result}'

    def make_order(self, amount_in_a_row):
        while self.amount > amount_in_a_row:
            if self.amount > amount_in_a_row:
                print('*' * amount_in_a_row)
            self.amount = self.amount - amount_in_a_row
            if self.amount < amount_in_a_row:
                print('*' * (self.amount % amount_in_a_row))


cell_1 = Cell(23)
cell_2 = Cell(2)
cell_3 = cell_1 - cell_2
print(cell_3)
cell_1.make_order(7)
