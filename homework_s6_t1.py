'''
1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
in
9

out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]

in
10

out
[28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
[24, 15, 23, 25]
'''

from random import randint

number = int(input("Введите число: "))

num_list = [randint(1,50) for i in range(number)]
print(f'Исходный список: {num_list}')
new_list = [num_list[n] for n in range(len(num_list)) if n != 0 and num_list[n-1]<num_list[n]]
print(f'Полученный список: {new_list}')
