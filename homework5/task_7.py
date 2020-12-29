import json


with open('task7.txt', 'r', encoding='UTF-8') as file:
    sum_profit = 0
    res = {}
    lines = file.readlines()
    for line in lines:
        name, form, income, outcome = line.split()
        profit = float(income) - float(outcome)
        res[name] = profit
        if profit > 0:
            sum_profit += profit

res['average_profit'] = round(sum_profit / len(lines), 2)

with open('task7.txt', 'w', encoding='UTF-8') as file:
    json.dump(res, file)