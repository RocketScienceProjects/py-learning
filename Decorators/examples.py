
# def being_polite(func):
#     def another():
#         print("Good Morning!")
#         func()
#     return another

import high

@high.being_polite
def greet():
    print("Hi there!!")

@high.being_polite
def rage():
    print("Go away...")


# greet()
rage()