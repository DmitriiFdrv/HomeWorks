# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
def calc(work_hours, money_hours, bonus):
    return (work_hours * money_hours) + bonus


work_hours = int(input('выработка в часах :'))
money_hours = int(input('ставка в час: '))
bonus = int(input('премия: '))
print('заработная плата сотрудника: ', calc(work_hours, money_hours, bonus))

# = int(input())
# = int(input())
# = int(input())
