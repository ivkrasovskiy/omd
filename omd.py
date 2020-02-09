def step(current_level=1):
    print(
        'Аналитик решил завести метрику в dma.metrics.'
    )

    prev_level = 0
    next_level = 0

    tree = {1: {'text': 'Сделал ли витрину с наблюдениями для своей метрики?', 'да': 2, 'нет': 3},
               2: {'text': 'Ну так сделай, чего же ты ждешь! Получилось?',  'да': 3, 'нет': 4},
               3: {'text': 'Отлично! А в файл dma.v_metric_observations добавил наблюдения?', 'да': 5, 'нет': 6},
               4: {'text': 'Старайся усерднее. Справился(-ась)?', 'да': 3, 'нет': 10},
               5: {'text': 'Ну ты просто секси. Осталось завести метрику в конфиге yaml. Готово?', 'да': 7, 'нет': 4},
               6: {'text': 'Это просто один крошечный UNION. Дело сделано?', 'да': 5, 'нет': 4},
               7: {'text': 'Все в восторге от тебя! А ты от metrics registry!'},
               10: {'text': 'Ваш пропуск заблокирован, вы уволены.'}
               }

    user_input = ''

    while user_input not in ('да', 'нет'):
        print('Ответьте да или нет на вопрос {}'.format(tree[current_level]['text']))
    user_input = input()
​
    new_level = tree[current_level][user_input]

    if tree[current_level][user_input]:
        return step2_umbrella()
    return step2_no_umbrella()
​
	if name == ' main ':
		step1()