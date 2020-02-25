from typing import Dict, List, Tuple


FIELD_WIDTH = 2
COLUMN_WIDTH = 4


def get_field_size() -> int:
    """
    Getting a field size from a user input and printing the field. 3 <= field size <= 5.
    If the input is incorrect - repeat.
    """
    while True:
        user_input = input()
        if not (user_input.isdigit() and 3 <= int(user_input) <= 5):
            print('The field size has to be between 3 and 5 \n')
        else:
            break

    return int(user_input)


def generate_field(field_size: int, lines_names: str) -> Tuple[Dict, List]:
    """
    Generating two fields for game. Different types fit better different checks.
    """
    list_field = []  # Список вида [[1,0,1], [-1,0,-1], [0,0,0]], где 1 соотвествует X, -1 - O, 0 - поле не занято
    dict_field = dict()  # Словарь хранит пары вида {a1: (0,0), a2: (0,1), a3: (0, 2), b1: (1,0) ..., c3: (2,2)}

    for i in range(field_size):
        current_row = []
        for j in range(field_size):
            current_row.append(0)

            dict_key = lines_names[i]  # буквенная часть ключа
            dict_key += str(j + 1)  # числовая часть ключа
            dict_field[dict_key] = (i, j)

        list_field.append(current_row.copy())
        del current_row

    # dict_field = {'a1': (0, 0), 'b1': (1, 0), 'a2': (0, 1), 'c3': (2, 2)}
    return dict_field, list_field


def draw_field(game_state: Dict, lines_names: str, draw_map: Dict) -> str:
    """
    Drawing the field of a fixed size.
    """
    scheme = ''
    field_size = len(game_state)

    print('\nCurrent field scheme: \n')

    for i in range(FIELD_WIDTH * field_size):  # Оставляем место под разделители строк
        for j in range(COLUMN_WIDTH * field_size):  # Оставляем место под символы внутри столбца
            scheme += pixel_drawer(game_state, i, j, lines_names, draw_map)
        scheme += '\n'  # переносим строку

    return scheme


def pixel_drawer(game_state: List[List], row: int, column: int, lines_names: str, draw_map: Dict) -> str:
    """
    Solving what symbol to draw based on a position in a scheme.
    """
    #   1   2   3
    # a   |   |
    #  -----------
    # b   |   |
    #  -----------
    # c   |   |

    # Понимать остатки от деления и целочисленное деление нужно глядя на картинку выше.
    # Нумерация идет со столбца, содержащего буквы a,b,c

    if row == 0:  # Обработка первой строки
        if column % 4 == 2:  # пишем 1,2,3,4,5 в названиях столбцов
            return str(column // 4 + 1)  # нумерация идет с 0, поэтому прибавляем единицу
        else:
            return ' '
    elif column == 0:  # Обработка первого столбца
        if row % 2 == 1:  # пишем a,b,c,d,e в названиях строк
            return lines_names[row // 2]
        else:
            return ' '
    elif row % 2 == 0:  # рисуем разделители строк
        return '-'
    elif column % 4 == 0 and column // 4 >= 1:  # рисуем вертикальные черточки
        return '|'
    elif column % 4 == 2:  # заполняем схему X или O
        return draw_map[game_state[row // 2][column // 4]]
    else:
        return ' '


def make_turn(map_field: Dict, game_state: List[List], player: int,
              lines_names: str, draw_map: Dict, move_counter: int, players_dict: Dict) -> bool:
    """
    Making a turn and check what next.
    """
    print('Make a turn {} player, enter a position on the field \n'.format(players_dict[player]))

    while True:
        position = input()
        cell = map_field.get(position)
        if cell is not None:  # Если игрок попал в поле
            #             print(game_state)
            cell_state = game_state[cell[0]][cell[1]]  # Смотрим, что лежит по координатам в поле
        else:
            cell_state = None

        if not check_turn(cell, cell_state):  # Проверка: поле занято или игрок назвал чушь
            continue
        else:
            move_counter += 1
            row, column = cell
            game_state[row][column] = player  # Записываеми ход игрока 1 или -1. Первый игрок 1, второй игрок -1, см. players_dict
            print(draw_field(game_state, lines_names, draw_map))  # Рисуем поле
            if check_win(cell, game_state, player):  # Проверяем, не случилось ли выигрыша после хода
                print('{} player has won!'.format(players_dict[player]))
                return 0
            elif move_counter == (len(game_state)) ** 2:  # Отходили максимум ходов
                print('Draw! What a fight!')
                return 0
            else:
                return player * (-1)  # Меняем игрока. Первый игрок 1, второй игрок -1, см. players_dict


def check_turn(cell, cell_state) -> bool:
    """
    Checking if a turn fits the field and a cell (defined by position) is free.
    """
    if cell is None or cell_state != 0:
        error_message(cell)
        return False
    else:
        return True


def error_message(cell: Tuple) -> int:
    """
    Messaging that a player can't make a move and a reason why.
    """
    if cell is None:
        print('Position is wrong (out of the field), try another move')
        return -1
    else:
        print('Current cell is busy already, try another move')
        return 0


def check_win(cell: Tuple, game_state: List[List], player: int) -> bool:
    """
    Checking if that's the last move and the game is over.
    """
    # Игра заканчивается, например когда первый собрал три едициы в столбце/строке или второй три минус единицы.
    # Это эквивалентно тому, что модуль суммы по столбцу/строке равен тройке (размерности игры).
    if abs(sum(game_state[cell[0]])) == len(game_state) or \
            abs(sum((row[cell[1]] for row in game_state))) == len(game_state):  # Проверка сумм по строке или по столбцу.
        return True
    # Также игра заканчивается, когда сумма диагональных элементов равна 3 (размерности игры).
    if cell[0] == cell[1]:  # Проверка главной диагонали
        return abs(sum(row[i] for i, row in enumerate(game_state))) == len(game_state)
    # Также игра заканчивается, когда сумма побочных диагональных элементов равна 3 (размерности игры).
    elif cell[0] + cell[1] == len(game_state) - 1:  # Проверка побочной диагонали
        return abs(sum(row[len(game_state) - i - 1] for i, row in enumerate(game_state))) == len(game_state)
    else:  # все условия мимо, не победа
        return False


if __name__ == '__main__':
    """
    Launching funtions one by one
    """
    print('Welcome to the game TicTacToe!\nPlease, enter field size from 3 to 5\n')
    lines_names = 'abcde'  # Названия строк в схеме
    draw_map = {0: ' ', 1: 'X', -1: 'O'}  # Отображения чисел в текст для рисовалки карты
    players_dict = {1: 'First', -1: 'Second'}  # Расшифровка игроков
    field_size = get_field_size()
    dict_field, list_field = generate_field(field_size, lines_names)  # Генерируем числовое и текстовое поле
    current_player = 1
    counter = 0

    print(draw_field(list_field, lines_names, draw_map))  # Drawing map

    while True:
        current_player = make_turn(dict_field, list_field, current_player, lines_names,
                                   draw_map, counter, players_dict)
        counter += 1  # Счетчик ходов. Если достигает квардрата длины поля - ничья
        if current_player == 0:  # Условие победы или ничьи
            break
