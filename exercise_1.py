"""
Задача 1.   Даны два списка,  нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.

Для анализа алгоритмов используем библиотеку timeit, чтоб засечь время выполнения каждой функции.
Сложность O(i + y): i, y - количество элементов в первом и во втором списках соответственно.
"""
import timeit


def func1(A: list, B: list) -> list:
    '''
    Преобразуем второй список во множество.
    Используем стандартный оператор in для поиска по списку.
    :return: list
    '''
    setB = set(B)
    index = 0
    for i in A:
        if i not in setB:
            A[index] = i
            index += 1
    return A[:index]

def func2(A: list, B: list) -> list:
    '''
    С использованием стандартного оператора in для поиска по списку.
    :return: list
    '''
    return [i for i in A if i not in B]

def func3(A: list, B: list) -> list:
    '''
    С использованием функции any
    :return: list
    '''
    C = []
    for i in A:
        if not any(element in i for element in B):
            C.append(i)
    return C


def func4(A: list, B: list) -> list:
    '''
    Поиск с помощью перебора в цикле
    :return: list
    '''
    C = []
    for i in A:
        flag = False
        for y in B:
            if i == y:
                flag = True
        if not flag:
            C.append(i)
    return C


if __name__ == '__main__':
    A = [str(n) for n in range(1000)]
    B = [str(n) for n in range(100, 1100)]

    print("# Вариант №1 -------------------")
    start_time = timeit.default_timer()
    C = func1(A, B)
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №2 -------------------")
    start_time = timeit.default_timer()
    C = func2(A, B)
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №3 -------------------")
    start_time = timeit.default_timer()
    C = func3(A, B)
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №4 -------------------")
    start_time = timeit.default_timer()
    C = func4(A, B)
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)
