class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return my_date

    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2021:
                    return f'верно'
                else:
                    return f'неверный год'
            else:
                return f'неверный месяц'
        else:
            return f'неверный день'

    def __str__(self):
        return f'сегодня {Date.extract(self.day_month_year)}'


today = Date('15-01-2021')

print(today)
print(Date.valid_date(10, 12, 2030))
print(today.valid_date(18, 20, 2001))
print(Date.extract('18-01-2021'))
print(today.extract('18-01-2040'))
