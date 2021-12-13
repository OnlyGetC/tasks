class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
    def __add__(self, other):
        return NutritionInfo(self.proteins + other.proteins, self.carbs + other.carbs, self.fats + other.fats)
    def __str__(self):
        return f"Nutrition p {self.proteins}, c {self.carbs}, f {self.fats}"
    def __mul__(self, val):
        return NutritionInfo(int(self.proteins * val), int(self.carbs * val), int(self.fats * val))
    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

egg = NutritionInfo(1, 2, 3)
pastila = NutritionInfo(1, 2, 3)
tvorog = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)
print(egg + pastila)
breakfast = apple * 3
print(breakfast)