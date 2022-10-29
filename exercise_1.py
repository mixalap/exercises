"""
Задача 1.   Даны два списка,  нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.
Для проверки эффективности алгоритма используем библиотеку timeit, чтоб засечь время выполнения каждой функции.
"""
import timeit

def func1():
    '''
    С использованием стандартного оператора in
    для поиска по списку.
    :return: list
    '''
    A = [str(n) for n in range(1000)]
    B = [str(n) for n in range(100,1100)]
    return [i for i in A if i not in B]

def func2():
    '''
    С использованием функции any
    :return: list
    '''
    A = [str(n) for n in range(1000)]
    B = [str(n) for n in range(100,1100)]
    C = []
    for i in A:
        if not any(element in i for element in B):
            C.append(i)
    return C


def func3():
    '''
    Поиск с помощью перебора в цикле
    :return: list
    '''
    A = [str(n) for n in range(1000)]
    B = [str(n) for n in range(100,1100)]
    C = []
    for i in A:
        flag = False
        for y in B:
            if i == y:
                flag = True
        if not flag:
            C.append(i)
    return C

def func4():
    '''
    Проверяем, сможем ли ещё ускорить процесс применив функцию map для генерации списка.
    :return: list
    '''
    A = list(map(str, range(1000)))
    B = list(map(str, range(100,1100)))
    return [i for i in A if i not in B]

if __name__ == '__main__':
    print("# Вариант №1 -------------------")
    start_time = timeit.default_timer()
    C = func1()
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №2 -------------------")
    start_time = timeit.default_timer()
    C = func2()
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №3 -------------------")
    start_time = timeit.default_timer()
    func3()
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)

    print("# Вариант №4 -------------------")
    start_time = timeit.default_timer()
    func4()
    print(C)
    print('Время выполнения: ', timeit.default_timer() - start_time)