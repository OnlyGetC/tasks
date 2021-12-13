import statistics as stat # Импортируем библитотеку чтоб было проще считать
with open('text.txt', 'w', encoding='utf-8') as f: # открываем и создаем файл
    text = '''Иванов О. 4 
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 1
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4
'''
    f.write(text) # Записываем
print('_________________________')
print('Ученики и их оценки:')
print('_________________________')
with open('text.txt', 'r', encoding='utf-8') as reading: # проверямем что записалось
    reading = reading.read()
    print(reading)
print('_________________________')
print('Отстающие ученики:')
print('_________________________')
with open('text.txt', 'r', encoding='utf-8') as scoring:
    reading = scoring.read().split('\n')[0:-1]
    scores = [i[-1] for i in reading]
    scores_median = stat.median(scores) # подсчет медианной оценок с помощью библиотеки статистики
    bad_students = [i for i in reading if i[-1] < scores_median] # находим учеников с плохими оценками и выводим их
print(f'Плохие ученики: {bad_students}')
print(f'Средний балл: {scores_median}')
print('_________________________')