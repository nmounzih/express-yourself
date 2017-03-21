import re


def binary(number):
    return re.search(r'^(0|1[01]*)$', number)


def binary_even(number):
    return re.search(r'^(0|1[01]*0)$', number)


def hex(text):
    return re.search(r'^[0-9A-Fa-f]+$', text)


def word(text):
    return re.search(r'^\b[\w-]*[A-Za-z]+\b$', text)


def words(text, count=None):
    result = re.findall(r'\b[\w-]*[A-Za-z]+\b', text)
    return len(result) == count if count else result


def phone_number(number):
    return re.findall(r'[(9][\d]+', number)
    #return re.search(r'\(?[0-9]{3}\)?[\D]?[0-9]{3}[\D]?[0-9]{4}', number)


def money(number):
    return re.search(r'^\$[0-9]{1,3}?(\,?[0-9]{3}*)(\.[0-9]{2})?$', number)


def zipcode(number):
    return re.findall(r'^[0-9]{5}(?:-[0-9]{4})?$', number)
    #return re.search(r'^[0-9]{5}(-[0-9]{4})?$', string)


def date(number):
    return re.findall(r'^[0-9]{1,4}[-/][\d][-/0-9]+', number)
