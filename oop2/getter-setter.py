
# getters and setters in python3

class Human():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age     # specifying that the age is private attibute to respect

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be a negative number")

    def full_name(self):
        print(f"{self.first} {self.last}")

help(Human)

tomba = Human("tomba", "okram", 45)
# print(tomba._age)  This is not conforming to the standard
print(tomba.age)  #calling the getter method as an attribute (without the parentheses)
tomba.age = 33
print(tomba.age)
