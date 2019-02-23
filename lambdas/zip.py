def interleave(str1, str2):
    output = zip(str1, str2)
    a = list(sum(output, ()))
    str1 = ''.join(a)
    return str1

print(type(interleave("hi", "ha")))