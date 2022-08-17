# class User(object):
# class User:
#     # count = 1
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age, house):
#         self.house = house
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         print(self.name)


# user1 = User('Max', 15)
# user2 = User('Olha', 18)
# user1.house = 55
# User.count = 8
#
# print(user1.house)
# print(user2.count)
#
# print(user1.name)
# # User.count = 7
# # print(User.count)


# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     def get_name(self):
#         return self._name
#
#
# user = User('Max', 15)

# class Car:
#     def __init__(self, bland):
#         self.bland = bland
#
#
# class Tools:
#     def start(self):
#         print('Brbrbrbr')
#
#     def stop(self):
#         print('Pff')
#
#
# class SuperCar(Car, Tools):
#     def __init__(self, bland, speed):
#         super().__init__(bland)
#         self.speed = speed
#
#
# car = SuperCar('BMW', 255)
# car.start()
# print(car.bland)

# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)

#
# user = User('Max')
#
# user.name = 'Olha'
# del user.name
# print(user.name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Olga'
# print(user.name)
# del user.name
# print(user.name)


# class Shape:
#     def area(self):
#         pass
#
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.c * self.b / self.a
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(1, 2), Triangle(3, 4, 6)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.c * self.b / self.a
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(1, 2), Triangle(3, 4, 6)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())
#
# # for i in range(50):
# #     pass
# #
# # print()

# class User:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def get_count(cls):
#         # return User.count
#         return cls.count


class User:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __truediv__(self, other):
        return self.age / other.age

    def __len__(self):
        return len(self.name)


# user = User('Max', 15)
# users: list[User] = [User('Max', 15), User('Olha', 15)]
# print(users)

max = User('Max')
olha = User('Olha', 15)

print(max + olha)
print(max - olha)
print(max * olha)
print(max / olha)

print(len(olha))

