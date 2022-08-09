# ДЗ

# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# str = 'as 23 fdfdg544'
# 2,3,5,4,4        #вивело в консолі.
# str=input('введіть строку-')
# for element in str:
#     if element=='1' or element=='2' or element=='3'or element=='4'or element=='5'or element=='6'or element=='7'or element=='8' or element=='9'or element=='0':
#         print(element,end='')

# print(', '.join(i for i in str if i.isdigit()))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34'
# введена строка
#   23, 544, 34              #вивело в консолі
# st=input('введіть строку:')

# print(''.join(i if i.isdigit() else ' ' for i in st).split())

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# print([i.upper() for i in greeting])
#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# print([i**2 for i in range(50) if i%2])
#
# function
#
# - створити функцію яка виводить ліст
# l=['1','2','3','4']
# def func_print_list(l):
#     for i in l:
#         print(i+',',end='')
# func_print_list(l)
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def func_max(a,b,c):
#     res=max(a,b,c)
#     print(res)
# func_max(2,4,6)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def func_min_max(*args):
#     print(max(args))
#     return min(args)
# print(func_min_max(1, 2, 3, 4, -6))
# - створити функцію яка повертає найбільше число з ліста
# l=[1,2,4,56,-7]
# def func_return_max(l):
#     return max(l)

# print(func_return_max(l))

# - створити функцію яка повертає найменьше число з ліста
l = [1, 2, 4, 56, -7]
# def func_return_min(l):
#     return min(l)
#
#
# print(func_return_min(l))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def func_sum(l):
#     return sum(l)
#
#
# print(func_sum(l))
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def func_ser(l):
#     return sum(l)/len(l)
#
#
# print(func_ser(l))
#
#
#
# ################################################################################################
# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
# def func_min(list):
#     print(min(list))
#
# func_min(list)
#   - видалити усі дублікати
# def func_dubl(list):
#     res=set(list)
#     return res
#
# print(func_dubl(list))
#   - замінити кожне 4-те значення на 'X'
# def func_swap_x(list):
#     print(['X' if not((i+1)%4) else v for i,v in enumerate(list)])
#
#
# func_swap_x(list)
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# def func_squre(a):
#     for i in range(a):
#         if i == 0 or i == a - 1:
#             print("*" * a)
#         else:
#             print('*' + " " * (a - 2) + '*')
#
#
# func_squre(50)

# 3) вывести табличку множення за допомогою цикла while

# 4) переробити це завдання під меню
