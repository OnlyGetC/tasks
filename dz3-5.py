from random import random
N = 10 #количесто элементов списка
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 50) # заполняем список рандомными числами
print(arr) # Выводим чтоб посмотреть что там
for i in range(N-1):  # Проверяем на уникальность
    for j in range(i+1, N):
        if arr[i] == arr[j]:
            print("Есть одинаковые")
            quit()
print("Все элементы уникальны")