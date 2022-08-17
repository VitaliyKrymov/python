"""
Создать класс Rectangle:
-конструктор принимает две стороны x,y
-описать арифметические методы:
  + сума площадей двух экземпляров класса
  - разница площадей
  == или площади равны
  != не равны
  >, < меньше или больше
  при вызове метода len() подсчитывать сумму сторон
"""


class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.array = x * y

    def __add__(self, other):
        return self.array + other.array

    def __sub__(self, other):
        return self.array - other.array

    def __eq__(self, other):
        return self.array == other.array

    def __ne__(self, other):
        return self.array != other.array

    def __gt__(self, other):
        return self.array > other.array

    def __lt__(self, other):
        return self.array < other.array

    def __len__(self):
        return self.y * 2 + self.x * 2


rectangle1 = Rectangle(2, 3)
rectangle2 = Rectangle(10, 20)

print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(rectangle1 > rectangle2)
print(rectangle1 < rectangle2)
print(len(rectangle1))
"""
создать класс Human (name, age)
создать два класса Prince и Cinderella:
у золушки должно быть имя возраст и размер ноги
у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
и метод класса который будет показывать это количество
"""


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name: str, age: int, shoe_size: int):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.size == self.shoe_size:
                print(cinderella)
                break


cinderellas: list[Cinderella] = [
    Cinderella('olha', 15, 35),
    Cinderella('kira', 20, 30),
    Cinderella('Kamila', 18, 32),
    Cinderella('ira', 15, 28),
]

prince = Prince('Kokos', 25, 30)
prince.find_cinderella(cinderellas)

"""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
    класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
Приклад:
Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))
    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()

для перевірки ксассів використовуємо метод isinstance, приклад:
"""

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Magazine(Printable):
    def __init__(self, name: str):
        self._name = name

    def print(self):
        print(self._name)


class Book(Printable):
    def __init__(self, name: str):
        self._name = name

    def print(self):
        print(self._name)


class Main:
    printable_list: list[Printable] = []

    @classmethod
    def add(cls, new_item: Printable):
        # if isinstance(new_item, Book) or isinstance(new_item, Magazine)
        if isinstance(new_item, (Book, Magazine)):
            cls.printable_list.append(new_item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('m1'))
Main.add(Magazine('m2'))
Main.add(Magazine('m3'))
Main.add(Magazine('m4'))

Main.add(Book('b1'))
Main.add(Book('b2'))
Main.add(Book('b3'))

Main.add(prince)

Main.show_all_books()

print('*' * 40)

Main.show_all_magazines()

print(Main.printable_list)
Footer
