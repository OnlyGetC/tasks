def print_dict(my_dict):
    for i in my_dict.items():
        print(f'Key "{i[0]}" Value is {i[1]}')
def print_list(my_list):
    for i in range(len(my_list)):
        print(i+1,my_list[i])
        i = i + 1
def print_overlord(mydict):
    for i in mydict.items():

        if isinstance(i[1], dict):
            print_dict(i[1])

        elif isinstance(i[1], list):
            print_list(i[1])

        else:
            print(f'значение: {i[1]}')
d = dict(key1=1, key2=[1, 2, 3, 4],
            key3='Hello',
            key4={"ciao":"Mondo", "Привет": "О дивный мир"})
print_overlord(d)