print ('Hello python ')

# sdkjfhskjdfh

# i = 3
# f = 1.3
# b = True  # False
# s = "some text"
# n = None

# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))

# some_vae

# a = b = c = 10
#
# print(a, b, c)

# num = 'hhh'
#
# num = int(num)
#
# print(type(num))
# print(num)


# int()
# float()
# bool()
# str()


# a = 0
# a++
# a += 1
a = 4
b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(14/3.3)
#print(round(a/b))

# print(3%2)
# print(2525**2525)


# s = input("Введіть ім'я: ")
# print(s)


# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)
#
# print(a is b)
# print(a is not b)
# a =3
# b =4
# # if 5>4 or 2<3:
# if a>b:
#     print('yes')
# elif b>a:
#     print('dfsdf')
# else:
#     print('no')


# num = int(input('Enter number: '))
#
# res = 'yes' if num>5 else 'no'
#
# print(res)


# list
#################################

# l = [1, 2, 3, 4, 5, 6, 8]

# print(l[0])
# # print(l[34])
# print(l[-2])
# l[1] = 25
# print(l)
#
# print(len(l))

# a = l
#2 = [7, 8, 9]
# l = list()

# l.append(1)
# l2 = l.copy()
# l.insert(3333, 55)
# pop = l.pop()
# pop = l.pop(0)
# print(pop)
# l.remove(2)
# l.extend(l2)
# l +=l2
# print(l)
# print(l.index(33))
# print(l.count(3))
# l.reverse()
# l.sort(reverse=True)
# l.clear()
# print(l)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
#
# res = l1[::-1]
#
# print(res)

# tuple()

# my_tuple = (1, 2, 4, 5)
# my_tuple.count(2)
# my_tuple.index(1)
# my_tuple[0] = 5
# print(my_tuple)

# dictionary

# dic = {
#     'name': 'Max',
#     'age': 15,
#     'status': False
# }

# dic['name'] = 45
# print(dic['name'])
# print(dic.get('name1', 'sdfjkhksjdfh'))
# print(dic)
#
# # dic.clear()
# print(dic.items())
# print(dic.keys())
# print(dic.values())

# pop = dic.pop('name')
# print(pop)
# popitem = dic.popitem()
# print(popitem)
# print(dic)

# dic = {
#     'name': 'Max',
#     'age': 15,
#     'status': False
# }
# dic.setdefault('name1', 'Vasia')
# dic.update({'house':2})
# dic |= {'house':8}
# print(dic)


# SET
# set()
# s = {1, 2, 3, 5, 1, 2, 7, 8, 2}
# s1 = {}
# s1 = set()
# print(type(s1))
# print(s)
#
# s = set()
# s.add(1)
# s.add(1)
# s.add(2)
#
# print(s)

# # l = [1, 2, 3, 2, 4, 6, 2]
# # s = set(l)
# # l = list(s)
# # print(l)
# set_1 = {10,12,3,7}
# set_2 = {1,2,3,4,5,6,7}
# #
# # print(set_1.issuperset(set_2))
# # print(set_1.issubset(set_2))
# print(set_1.isdisjoint(set_2))
# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))
# set_1.update(set_2)
#
# print(set_1)
# # print(set_1[0])
#pop = set_2.pop()
#print(pop)
# # set_1.remove(22)
# # set_1.discard(2)
# print(set_1)


# string

#string = "sdfhksdfh\""
#print(string)
# a='*'

# print(a*50)
#name = 'Max'
#age = 18
#weight = 75.5
#
# string = 'Hello, my name is Max, I\'m 18 and my weight 75.5kg'
# string = 'Hello, my name is' + name + ', I\'m' + str(age) + ' and my weight ' + str(weight) + 'kg'
# string = 'Hello, my name is %s, I\'m %d and my weight %fkg' % (name, age, weight)
# string = 'Hello, my name is {}, I\'m {} and my weight {}kg'.format(name, age, weight)
# string = 'Hello, my name is {name}, I\'m {age} and my weight {weight}kg'.format(age=age, weight=weight, name=name)
# string = 'Hello, my name is {name}, I\'m {age} and my weight {weight}kg'.format(age=age, weight=weight, name=name)
#string = f'hello, my name is {name}, I\'m {age} and my weight {weight}kg'

# # print(string.index('l'))
# # print(string.count('l'))
# # print(string.capitalize())
# # print(string.lower())
# # print(string.islower())
# # print(string.isupper())
#
# print('hello world'.title())
# print('Hello world'.swapcase())
# print('Helloworld'.isalpha())
# print('123s'.isdigit())
# print('123s'.startswith('12'))
# print('123s'.endswith('12'))
#
# print(['   sdfsdf    '.strip()])
# print(['aaa   sdfsdf    aaa'.strip('a ')])
#
# print(['   sdfsdf    '.lstrip()])
# print(['   sdfsdf    '.rstrip()])
#
# # print('Hello world 1'.split('')) # error
# print('Hello-world-1'.split('-'))
# # print(list('Hello world 1'))
#
# # print('one is two'.partition('is'))
#
# print('hello worlld'.replace('ll', 'bb'))
#
# print(''.isspace())
# print('hello'[:5:2])


# print(min([1,2,3,5]))
# print(max(2,3,4,5,6))
# print(sorted([1,2,3,4,6], reverse=True))
# print(pow(2,25))


# func


# def func(name, age=14, *args, **kwargs):
#     # print('hello', name, sep='-', end='')
#     print('hello', name, age)
#     print(args)
#     print(kwargs)
#     return 5
#
#
# i = func('Max', 18, 'sdf', 23, 34, house=15, status=False)
# print(i)

#
# def func(*args):
#     print(args)
#
#
# l = [1, 2, 3, 4]
# func(*l)


# i = 5
#
# while i > 8:
#     i -=1
#     print(i)
# else:
#     print('finish')


#l = [1, 2, 3, 4]

# for item in l:
#     print(item)


# for i in range(2,10, 2):
#     print(i)


# for i, v in enumerate(l):
#     print(i, v)


# user = {
#     'name':'max',
#     'age':18
# }
#
# for k,v in user.items():
#     print(k, v)
#
#
# print(33 in l)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # l1 = [i**2 for i in l]
# l1 = [i ** 2 if i == 4 else str(i) for i in l if i % 2 == 0]
# print(l1)


# dict_1 = {'Name': 'max', 'AgE': 14}
#
#
# dict_2 = {k.lower():v for k,v in dict_1.items()}
#
# print(dict_2)


# l = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]
#
# res = [i for j in l for i in j]
#
# res2 = []
# for j in l:
#     for i in j:
#         res2.append(i)
#
# print(res)
# print(res2)


# for i in range(5):
#     pas

# print(i)

#print('-'.join(['1', '2', '3', '4']))

