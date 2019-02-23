# class attributes

class MyPet:
    allowed = ["Lion", "Tiger", "Cobra"]   # class attributes

    def __init__(self, name, species):
        if species not in MyPet.allowed:
            raise ValueError(f"{species} cannot be a pet")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in MyPet.allowed:
            raise ValueError(f"{species} cannot be a pet")
        self.species = species

Tiger = MyPet("Zoe", "Tiger")
Tiger.set_species("Lion")
print(Tiger.name)
print(Tiger.species)
