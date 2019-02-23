## print numbers from 1 to 20
## multiple of 3 - "Fizz"
## multiple of 5 - "Buzz"
## mulitple of 3 & 5 - "FizzBuzz"


for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

