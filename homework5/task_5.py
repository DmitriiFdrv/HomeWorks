with open('task5.txt', 'w+', encoding='UTF-8') as file:
    numb = input('введите числа через пробел \n')
    file.writelines(numb)
    fin = numb.split()
print(sum(map(int, fin)))