import re


def binary(number):
    return re.findall(r'[0-1]+', number)


def binary_even(number):
    return re.findall(r'^[0-1]{0,16}[0]$', number)


def hex(text):
    if len(re.findall(r'[0-9A-Fa-f]+', text)) != 1:
        return False
    else:
        return True


def word(text):
    if len(re.findall(r'[A-Z-a-z]+', text)) != 1:
        return False
    else:
        return True


# def words(text, count=None):
#     if count:
#         if re.findall(r'[A-Z-a-z]+', text) != count:
#             return False
#     else:
#         return re.findall(r'[A-Z-a-z]+', text)


def phone_number(number):
    return re.findall(r'[(9][\d]+', number)


def money(number):
    return re.findall(r'^[$][\d]+', number) or re.findall(r'^[$][\d]+[.][\d]+', number)
