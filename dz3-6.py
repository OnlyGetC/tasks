from random import random
N = 10 #количесто элементов списка
list = [0] * N
for i in range(N):
    list[i] = int(random() * 50) # заполняем список рандомными числами

print(list)
def print_list(my_list):
    for i in range(len(my_list)):
        print(i+1,my_list[i])
        i = i + 1
print_list(list)