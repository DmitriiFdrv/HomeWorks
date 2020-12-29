rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_file = []
with open('task4.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        i = i.split(' ', 1)
        my_file.append(rus[i[0]] + ' ' + i[1])
    print(my_file)

with open('task4_new.txt', 'w', encoding='UTF-8') as file2:
    file2.writelines(my_file)