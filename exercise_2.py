"""
Задача 2.  Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
"""

def del_zero_digit(array) -> list:
    """
    Перезапишем массив, чтобы не использовать дополнительную память.
    :param array:
    :return: list
    """
    index = 0
    for i in array:
        if i != 0:
            array[index] = i
            index += 1
    return array[:index]

if __name__ == '__main__':
    arr = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
    print("input: ", arr)
    print(del_zero_digit(arr))