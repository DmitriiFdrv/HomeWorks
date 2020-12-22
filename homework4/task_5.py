# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

l = [el for el in range(99, 1001) if el % 2 == 0]

def calc(prev_el, el):
    return prev_el * el

print(reduce(calc, l))

print(reduce(calc, [el for el in range(99, 1001) if el % 2 == 0]))
