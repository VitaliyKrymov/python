# for i in range(10):
#     res = i+1
#     print(res)
#
# def show_var(i):
#     i **= 2
#     return i
#
#
# for i in range(10):
#     var = show_var(i)
#     print(var)

# class MyException(Exception):
#     pass
#
#
# try:
#     try:
#         print(8 / 0)
#     except ZeroDivisionError:
#         raise MyException
#     # except NameError:
#     #     print('error')
#     except Exception:
#         print('some exc')
#
# except MyException:
#     print('my custom error')
#
# print('dfdfdf')


# try:
#     input('Press Enter')
#     # print(8/0)
# # except KeyboardInterrupt:
# #     print()
# #     print('exit')
# # except ZeroDivisionError as err:
# #     print(err)
# # else:
# #     print('ok')
# finally:
#     print('finish')


# l = [i for i in range(50000000)]
#
# input()

# g = (i for i in range(5))

# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# print(g[7])

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen(name: str):
#     for ch in name:
#         yield ch
#         yield 1
#         yield 3
#         print('next')
#         return 'returnsdsdsdsd'
#
#
# g = gen('Max')
#
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as err:
#     print(err)


# def gen1(n):
#     for i in range(n):
#         yield f'worker[{i}] -- team1'
#
#
# def gen2(n):
#     for i in range(n):
#         yield f'worker[{i}] -- team2'
#
#
# team1 = gen1(5)
# team2 = gen2(7)
#
# teams = [team1, team2]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass
# import uuid
#
# def gen_jpg_file_name():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# name = gen_jpg_file_name()
#
# print(next(name))


# class MyRange:
#     def __init__(self, length: int):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration
#
#
# my_range = MyRange(5)

# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# for i in my_range:
#     print(i)

# file = open('1.txt', 'w')
#
# file.write('Hello World!!!')
#
# file.close()

# try:
#     file = open('1.txt')
#     try:
#         read = file.read()
#         print([read])
#     finally:
#         file.close()
# except Exception as err:
#     print(err)
# try:
#     with open('1.txt', 'r+') as file:
#         print(file.read())
#         file.write('finish')
#         print(file.tell())
#         file.seek(0)
#         print(file.read())
# except Exception as err:
#     print(err)


# try:
#     with open('1.txt', 'w') as file:
#         print('Hello Python', file=file)
# except Exception as err:
#     print(err)

import json

# user = {
#     'name': 'Max',
#     'age': 15
# }

# # try:
# #     with open('1.txt', 'w') as file:
# #         json.dump(user, file)
# # except Exception as err:
# #     print(err)
#
# try:
#     with open('1.txt', ) as file:
#         user = json.load(file)
#         print(user)
# except Exception as err:
#     print(err)


##################################################
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# user = User('Kokos', 15)

# try:
#     with open('1.txt', 'wb') as file:
#         pickle.dump(user, file)
# except Exception as err:
#     print(err)

# try:
#     with open('1.txt', 'rb') as file:
#         user: User = pickle.load(file)
#         print(user.name)
# except Exception as err:
#     print(err)

# try:
#     with open('origin.jpg', 'rb') as file, open('my_python.jpg', 'wb') as file2:
#         image = file.read()
#         file2.write(image)
# except Exception as err:
#     print(err)

# num = input('enter num: ')
#
# match num:
#     case '1':
#         print('1')
#     case '2':
#         print('2')
#     case _:
#         print('error')


# p = 'exit'
#
# match p:
#     case 'left'|'right' as action, value:
#         print(action, value)
#     case action, value:
#         print('aaaaaaaaaaaaaa', action, value)
#     case 'exit':
#         print('exit')
#     case _:
#         print('error')

user1 = {
    'name': 1,
    'age': 15,
    'status': True
}


#
# match user:
#     case {'name': str(name), 'age': 15 as age, 'status': True}:
#         print(f'{name=} {age=}')


class User:
    __match_args__ = 'name', 'age'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user2 = User('Kokos', 25)


def matcher(source: User | dict):
    match source:
        case User('Kokos' as name):
            print(name)
        case {'name': str(name)}:
            print(name)

matcher(user2)

