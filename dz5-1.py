class student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.group_number = group_number
    def get_Name(self):
        return self.name
    def get_Age(self):
        return self.age
    def get_Group_Number(self):
        return self.group_number
    def set_Name_Age(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    def set_Group_Number(self, new_group_number):
        self.group_number = new_group_number
    def get_Info(self):
        print(f'Student: {self.name}, {self.age}, {self.group_number} group')
student_1 = student(name = 'Ivan', age = 32, group_number = '10a')
student_2 = student(name = 'Petr',  group_number = '9b')
student_3 = student(name = 'Sergey', age = 53)
student_4 = student('Alex',12,'11c')
student_5 = student('Ilya',20,'IT')
student_1.get_Info()
