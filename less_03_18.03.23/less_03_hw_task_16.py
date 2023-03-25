"""
Задача 16:
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N].

Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""

n = int(input('Введите количество элементов массива: '))
a_i = list(input(f'Введите {n} значений элементов массива через пробел: ')
           .split(' '))
find_num_count = input(
    'Введите значение Х для подсчета его количества в массиве: ')

# вар.1 поиск и подсчет через сравнение
print('вар.1 поиск и подсчет через сравнение')
count = 0
for i in a_i:
    if i == find_num_count:
        count += 1
print(
    f'в массиве {a_i} элемент со значением "{find_num_count}" '
    f'встречается {count} раз(а)\n')

# вар.2 подсчет через словарь
print('вар.2 подсчет через словарь')
dict_count = {}
for i in a_i:
    if i in dict_count.keys():
        dict_count[i] += 1
    else:
        dict_count[i] = 1
if find_num_count not in dict_count.keys():
    print(f'Элемент со значением "{find_num_count}" ОТСУТСТВУЕТ в массиве {a_i}')
else:
    print(f'в массиве {a_i} элемент со значением "{find_num_count}" '
    f'встречается {dict_count[find_num_count]} раз(а)')
