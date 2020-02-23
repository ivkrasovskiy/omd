import re
from typing import Union, List, Tuple, Generator


def count_nonunique_elements(
        source_list: Union[List, Tuple]) -> int:  # 6 задача кол-во неуникальных элементов в массиве
    '''
    Count nonunique elements in tuple or list
    '''
    return len(source_list) - len(set(source_list))


# print(count_nonunique_elements((12,3,3,4,4,4)))


def filter_list(
        source_list: List) -> Generator:  # 7 задача фильтруем лист по условию (без конкретного условия непонятно)
    '''
    Filtering list wo filter
    '''
    return (l for l in source_list if l < 5)


# print(list(filter_list([12,3,3,4,4,4])))


def filter_list(string: str) -> str:  # 9 задача заменить несколько пробелов на один
    '''
    Deleting multiple spaces
    '''
    return re.sub(' +', ' ', string)


# print(filter_list('This is  a dirty string that has   to be purged'))


def filter_by_substring(source_list: List[str], substring: str) -> Generator:  # 10 фильтруем из листа со строками
    '''
    Filter list of string by substring, survives only those that include susbstring
    '''
    return (l for l in source_list if substring in l)


# print(list(filter_by_substring(['This is a', ' dirty string that has ', '  to be purged'], 'a')))


def check_coordinates(coordinates_array: List[tuple]) -> Generator:  # 11 оставляем только корректные координаты
    '''
    Latitude and longitude have to between [-90, 90] and [-180, 180] respectively
    '''
    return (coord_pair for coord_pair in coordinates_array if
            (-90.0 <= coord_pair[0] <= 90.0) &
            (-180.0 <= coord_pair[1] <= 180.0)
            )


# print(list(check_coordinates([(65, 144), (-98, 164), (-67, 214)])))


def find_wrong_bracets(string: str) -> int:  # 12 находим первую позицию неправильной скобки, иначе -1
    '''
    Find the first position of a wrong brace
    '''
    # Если единичка отвечает за левую скобку, ищем правую правее и наоборот
    brace_dict = {'{': ('}', 1), '}': ('{', -1), '(': (')', 1), ')': ('(', -1),
                  '[': (']', 1), ']': ('[', -1)}

    for i, s in enumerate(string):
        if s not in brace_dict:
            continue
        else:
            if brace_dict[s][1] > 0:  # проверка на левую скобку, тогда ищем правее
                # Проверка, что на соотв. месте с конца строки правильная скобка и то что скобки неперепутаны }{
                if (brace_dict[s][0] == string[-i - 1]) and (len(string) - i - 1 > i) or \
                        (i + 1) < len(string) and (brace_dict[s][0] == string[i + 1]):
                    # Строка выше проверяет ситуацию, когда скобки идут подряд
                    continue
                else:
                    return i
            else:  # тут обработка правой скобки, ищем левее
                # Проверка, что на соотв. месте с конца строки правильная скобка и то что скобки неперепутаны }{
                if (brace_dict[s][0] == string[-i - 1]) and (len(string) - i - 1 < i) or \
                        (i - 1) >= 0 and (brace_dict[s][0] == string[i - 1]):
                    # Строка выше проверяет ситуацию, когда скобки идут подряд
                    continue
                else:
                    return i

    return -1

# find_wrong_bracets('{}[][(])')
