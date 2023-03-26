"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def nums_input():
    try:
        num = int(input(f'Введите количество элементов множества: '))
    except ValueError:
        print('! Вы ввели не число или не целое число ! Повторите ввод.\n')
        return nums_input()
    return abs(num)


def summ_set(num):
    if num == 1:
        return num
    return num + summ_set(num - 1)


n = nums_input()
left_res = summ_set(n)
right_res = n * (n + 1) // 2
print(
    f'∑(1..n) -> {left_res} =?= n(n+1)/2 -> {right_res}: '
    f'{left_res == right_res}')

# если без "красоты" вывода - только проверка условия, то после строки 30
# можно давать только эту строку:
# print(summ_set(n) == n*(n+1)//2)
