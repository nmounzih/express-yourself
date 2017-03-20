import re


def words(text):
    if len(re.findall(r'[-A-za-z]+', text)) == 0:
        return
    else:
        return re.findall(r'[0-9-A-za-z]+', text)
