car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
def print_dict(my_dict):
    for i in my_dict.items():
        print(f'Key "{i[0]}" Value is {i[1]}')
print_dict(car)