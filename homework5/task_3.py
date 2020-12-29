with open('task3.txt', 'r', encoding='UTF-8') as file:
    money = []
    l = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            l.append(i[0])
            money.append(i[1])
print(f'оклад меньше 20000 {l}, среднии оклад {sum(map(int, money)) / len(money)}')
