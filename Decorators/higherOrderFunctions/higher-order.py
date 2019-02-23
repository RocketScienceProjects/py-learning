# # We can pass funcs as args to other funcs

# def sum(n, func):
# 	total = 0
# 	for num in range(1,n+1):
# 		total += func(num)
# 	return total

# def square(x):
# 	return x*x

# def cube(x):
# 	return x*x*x


# print(sum(3,cube))
# print(sum(3,square))

class Name:
  def __init__(self,name):
    self.name = name
  def __repr__(self):
	  return (f"This is {self.name}")
  def yell(self):
    print(f"My name is {self.name}")


a = Name("Sam")
b = a.yell
print(a)
print(b)