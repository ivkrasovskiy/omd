def step(current_level, tree):

    current_tree = tree
    current_tree[4]['да'] = tree[current_level].get('да')

    if current_tree[current_level].get('нет') is None:
        print('\n{}'.format(current_tree[current_level]['text']))
        return 0

    user_input = ''

    while user_input not in {'да', 'нет'} :
        print('Ответьте да или нет на вопрос:\n    {}'.format(current_tree[current_level]['text']))
        user_input = input().lower()

    new_level = current_tree[current_level].get(user_input)

    return new_level

if __name__ == '__main__':

    current_level = 1

    tree = {1: {'text': 'Сделал(-а) ли ты витрину с наблюдениями для своей метрики?', 'да': 3, 'нет': 2},
            2: {'text': 'Ну так сделай, чего же ты ждешь! Получилось?',  'да': 3, 'нет': 4},
            3: {'text': 'Отлично! А в файл dma.v_metric_observations добавил(-а) наблюдения?', 'да': 5, 'нет': 6},
            4: {'text': 'Старайся усерднее. Справился(-ась)?', 'да': None, 'нет': 10},
            5: {'text': 'Ну ты просто секси. Осталось завести метрику в конфиге yaml. Готово?', 'да': 7, 'нет': 4},
            6: {'text': 'Это просто один крошечный UNION. Дело сделано?', 'да': 5, 'нет': 4},
            7: {'text': 'Название метрики оканчивается на _canonical ?', 'да': 8, 'нет': 9},
            8: {'text': 'Все в восторге от тебя! А ты от metrics registry!'},
            9: {'text': 'Ты меня разочаровываешь... Ты исправил(-а) название?', 'да': 8, 'нет': 4},
            10: {'text': 'Ваш пропуск заблокирован, Вы уволены.'}
            }

    print('Добро пожаловать!')
    print('Аналитик(-чка) решил завести метрику в dma.metrics.')

while current_level != 0:
    current_level = step(current_level, tree)
