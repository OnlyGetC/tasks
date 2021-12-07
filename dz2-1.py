while True:
    month = int(input())
    month_spis = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']
    if month > 12 or month <= 0:
        print('Нет такого месяца')
    else:
        print(month_spis[month - 1])