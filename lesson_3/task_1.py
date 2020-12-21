
def val():
    a = int(input('Ввведите первое число: '))
    b = int(input('Ввведите второе число: '))
    c = a / b
#   if b == 0:
 #      print('на 0 делить нельзя')
    return c
print(f'ответ: {val():.3f}')
