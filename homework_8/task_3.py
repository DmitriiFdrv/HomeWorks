class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите данные: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                exit_cycle = input(f'Ввести еще раз? Y/N ')

                if exit_cycle == 'Y' or exit_cycle == 'y':
                    print(try_except.my_input())
                elif exit_cycle == 'N' or exit_cycle == 'n':
                    return f'конец'
                else:
                    return f'конец'


try_except = Error(1)
print(try_except.my_input())