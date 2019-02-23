# inheritence

class Animal:
    test = True
    def makes_sound(self, sound):
        print(f"This animal makes the {sound} sound")


class Pet(Animal): ## Passing the class "Animal" as an argument to the other class for inheritence
    pass


dog = Pet()
dog.makes_sound("woof")

