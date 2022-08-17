# from typing import Callable
#
#
# # def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(to_do: str) -> None:
#         nonlocal todo_list
#         todo_list.append(to_do)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
#
# add, all_todo = notebook()
#
# add('go to work')
# add('go to home')
# add('go to sleep')
#
# print(all_todo())
#
#
# def expanded_form(num: int) -> str:
#     st = str(num)
#     zero_count = len(st) - 1
#     return ' + '.join(v + '0' * (zero_count - i) for i, v in enumerate(st) if v != '0') + f' = {st}'
#
#
# print(expanded_form(50555))

def decor(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print(f'{count=}')
        # print(f'count={count}')
        func(*args, **kwargs)
        print('-' * 20)
        count += 1

    return inner

@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

func1()
func1()

func2()

func1()
func1()
func1()