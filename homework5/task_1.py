task1 = open('task1.txt', 'w')
line = input('Введите текст \n')
while line:
    task1.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

task1.close()
task1 = open('task1.txt', 'r', encoding='UTF-8')
content = task1.readlines()
print(content)
task1.close()