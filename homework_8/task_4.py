class Warehouse:

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return self.name

class Printer(Warehouse):
    def printer(self):
        return self.name

class Scanner(Warehouse):
    def scanner(self):
        return self.name

class Copier(Warehouse):
    def copier(self):
        return self.name

unit_1 = Printer('hp')
unit_2 = Scanner('Canon')
unit_3 = Copier('Xerox')
print(unit_1)
print(unit_2)
print(unit_3)
