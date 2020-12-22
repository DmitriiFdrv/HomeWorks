# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
l2 = [n for i, n in enumerate(l) if i > 0 and l[i] > l[i - 1]]
print(l2)