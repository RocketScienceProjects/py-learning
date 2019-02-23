class Train:
    def __init__(self, cars):
        self.cars = cars

    def __repr__(self):
        return f"{self.cars} car train"
    def __len__(self):
        return self.cars

    # def len(self):
    #     return self.cars


a = Train(2)
print(a)
print(len(a))
# print(a.len())