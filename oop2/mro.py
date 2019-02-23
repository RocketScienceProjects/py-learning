class Mother:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type
        
class Father:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type
        
class Child(Mother, Father):
    pass


help(Child)
        