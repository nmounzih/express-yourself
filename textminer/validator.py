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


def word():
