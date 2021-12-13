class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start_car(self):
        print("Автомобиль заведен")
    def stop_car(self):
        print("Автомобиль заглушен")
    def set_color(self, new_color):
        self.color = new_color
    def set_type(self, new_type):
        self.type = new_type
    def set_clear(self, new_year):
        self.year = new_year
    def get_info(self):
        return print(f'Car: {self.color} color, {self.type} type, {self.year} year')

car_1 = Car('Black', 'Coupe', 2000)
car_2 = Car('Yellow', 'Pickup', 1999)
car_3 = Car('Red', 'Sport-car', 1958)
car_4 = Car('Blue', 'Minivan', 1980)
car_5 = Car('Grey', 'Sedan', 2021)
car_5.get_info()