from functools import wraps
from time import time

def speed_test(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    start_time = time()
    result = fn(*args, **kwargs)
    end_time = time()
    elapse_time = end_time - start_time
    print(f"Elapse time is: {elapse_time}")
    return result
  return wrapper

@speed_test
def add(x,y):
    return x + y


a = add(10000000000000000000000000,556666666666666333333333)
print(a)


