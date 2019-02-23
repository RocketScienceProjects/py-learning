
class Human:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Race(Human): #inheritence
    def __init__(self, name, sex, age, color):
        super().__init__(name, sex, age)   # inheriting the attributes defined in the super class
        self.color = color


t = Race("jack", "M", "18", "white")

print(t.name)