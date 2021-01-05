class Matrix:
    def __init__(self, arr: list):
        self.arr = arr

    def __str__(self):
        print('Матрица:')
        for element in self.arr:
            print(element)
        return ''
        ### или же следующим образом, не знаю, какой в этом случае верный ###
        # for string in range(len(self.arr)):
        #     for element in self.arr[string]:
        #         print(element, end='   ')
        #     print(' ')
        # return ''


    def __add__(self, other):
        new_matrix = []
        for j in range(len(self.arr)):
            new_arr = []
            for i in range(len(self.arr[j])):
                element = self.arr[j][i] + other.arr[j][i]
                new_arr.append(element)
            new_matrix.append(new_arr)
        new_matrix = Matrix(new_matrix)
        return new_matrix


m_1 = Matrix([[1, 9, 3], [21, 12, 8], [20, 30, 50]])
m_2 = Matrix([[9, 1, 7], [9, 8, 12], [20, 30, 20]])
m_3 = m_1 + m_2
print(m_1)
print(m_2)
print(m_3)
