# class can have the __init__ method
# it gets called whenever an instance of the class is created

class User:
  def __init__(self, first, last):
    self.first = first
    self.last = last

p = User('tom','harris')

print(p.first)
print(p.last)
