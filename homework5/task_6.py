lesson = {}
with open('task6.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        subj, lect, pract, lab = line.split()
        lesson[subj] = float(lect) + float(pract) + float(lab)
print(f'общее количество занятий: \n {lesson}')
 #что-то пошло не так