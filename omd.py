def step1():
    print(
        'Аналитик решил завести метрику в dma.metrics.'
    )

    option = ''
    options = {1: {'text': 'Сделал ли витрину с наблюдениями для своей метрики?',
                   'options': 'Да'}

        'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
    option = input()
​
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()
​
	if name == ' main ':
		step1()