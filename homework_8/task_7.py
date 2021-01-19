class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = a + b

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}'

    def __str__(self):
        return f'c = {self.a} + {self.b}'


c_1 = ComplexNumber(15, -2)
c_2 = ComplexNumber(4, 9)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)