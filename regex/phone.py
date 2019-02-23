import re


def extract_phone(lines):
    pattern = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    res = pattern.findall(lines)
    return res


# a = extract_phone("this is my 360 702 6377 and 360-123-4345" )
# print(a)
