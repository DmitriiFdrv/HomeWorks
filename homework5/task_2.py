task2 = open('task2.txt', 'r', encoding='UTF-8')
content = task2.read()
print(f'Content: \n {content}')

task2 = open('task2.txt', 'r', encoding='UTF-8')
content = task2.readlines()
print(f'Ctpoku: \n {len(content)}')

task2 = open('task2.txt', 'r', encoding='UTF-8')
content = task2.readlines()
for i in range(len(content)):
    print(f'Simvol {i + 1} stroki: \n {len(content[i])}')

task2 = open('task2.txt', 'r', encoding='UTF-8')
content = task2.read()
content = content.split()
print(f'Kol-vo slov: \n {len(content)}')

task2.close()