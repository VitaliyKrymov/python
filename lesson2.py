
# arr = [1,2,3]
# user = {
#     'name':'max',
#     'age':15
# }
#
# del arr[1]
# del user['age']
# print(arr)
# print(user)


# tuple_1 = (1, 2, 3, 4, 5, 6, 7)

# a, b, *_ = tuple_1
# a, _, b,*_ = tuple_1
# *_, a, _, b = tuple_1

# print(a)
# print(b)
# print(_)

# a = 5
# b = 6
#
# a, b = (b,a)
#
# print(a)
# print(b)


user = {
    'name': 'max',
    'age': 18,
    # 'house':20
}

#
# def print_user(name, age, **kwargs):
#     print(name)
#     print(age)
#     print(kwargs)


# def print_user(name, age):
#     print(name)
#     print(age)
#     # print(kwargs)
#
# print_user(*user)
#
# arr = [1,2,3,4,5]
#
# def func(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# func(*arr)

# ####################################################################
# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
# @decor
# @decor
# def greeting(name):
#     print(f'Hello, {name}')
#
# # inner = decor(greeting)
# # inner('Max')
#
#
# greeting('Max')
# ####################################################################

# name = 'max'
#
# # print(globals())
#
# def func():
#     global name
#     name = 'olha'
#     print(name)
#     print(locals())
#
# func()
# print(globals())
# print(name)


# name = 'max'

# def a():
#     # name = 'Vasia'
#
#     def b():
#         nonlocal name
#         name = 'Oleg'
#         print(name)
#
#     b()
#     print(name)
#
#
# a()
# print(name)

# for i in range(5):
#     pass
#
# print(globals())
# ####################################################################

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# c1 = counter()
# c2 = counter()
#
# print(c1())
# print(c1())
#
# print(c2())
# print(c2())
# print(c2())
#
# print(c1())
# print(c1())
# print(c1())
# ####################################################################
arr = [1, 2, 3, 4]

# def add_one(value):
#     return  value +1

# const func = (a,b)=>a+b

# func = lambda a: a + 1

# m = map(lambda a: a + 1, arr)
#
# res = list(m)
#
# print(res)

# users = [
#     {
#         'name': 'max',
#         'age': 15
#     },
#     {
#         'name': 'kira',
#         'age': 25
#     },
#     {
#         'name': 'alina',
#         'age': 13
#     },
#
# ]
#
# f = filter(lambda x: x['age'] < 20, users)
#
# print(list(f))
#
# users.sort(key=lambda value: value['name'])
# print(users)

# import math

# # from math import sqrt
# # from math import * // bad practic
#
# from math import sqrt as q
# print(q(25))

from typing import List, Dict, Tuple, Union, Optional, Any, Callable, NewType, TypedDict


# def func(st: str) -> Union[int, str]:
# def func(st: str) -> int | str:
# def func(st: str) -> Optional[int]:
# def func(st: str) -> int | None:
#     return 4


def counter() -> Callable[[], int]:
    count = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner


c1 = counter()
count = c1()

print(count)

UserId = NewType('UserId', int)


def func(user_id: UserId):
    print(user_id)


func(UserId(12))

User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)

user: User = {'name': 'max', 'age': 15}