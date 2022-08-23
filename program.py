from math import sqrt

message = ('Добро пожаловать в самую лучшую программу'
            ' для вычисления квадратного'
            'корня из заданного числа')


def calculate_square_root(number:float):
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number:float):
    if your_number <= 0:
        return
    print(
            (f'Мы вычислили корень квадратный из введенного вами числа. '
                f'Это будет: {calculate_square_root(your_number)}')
        )


print(message)
calc(12)
