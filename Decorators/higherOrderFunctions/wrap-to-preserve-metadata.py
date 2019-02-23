from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        print(fn.__doc__)
        return fn(*args, **kwargs)   #why am i returning this?
    return wrapper

@log_function_data
def add(x,y):
    '''Adds 2 numbers and returns'''
    return x + y


# print(add(2,3))
print(add.__name__)
print(add.__doc__)