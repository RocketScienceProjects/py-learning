def yes_or_no():
    counter = 1
    while True:
        if counter % 2 == 0:
            yield 'no'
        else:
            yield 'yes'
        counter += 1

t = yes_or_no()

print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))