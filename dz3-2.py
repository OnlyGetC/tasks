inp = int(input('Введите количество желаемых раcширений '))
extentions = []
for inp in range(inp): # Цикл заполнения списка
    extentions.append(input('введите имя расширения '))
file_name = input('Введите имя файла ')
i = file_name.rfind('.')
for f in extentions:
    if f == file_name[i+1:]:
        print(f)
        k = 1;
        break
if k != 1:                               # если нужны определённые расширения
    print("Такого расширения не существует, првоерьте правильность ввода")