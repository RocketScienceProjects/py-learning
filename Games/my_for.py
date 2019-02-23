
def my_for(iterable, function):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            function(i)


my_for("apple", print)
        

