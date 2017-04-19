import re


def words(text):
    if len(re.findall(r'[-A-za-z]+', text)) == 0:
        return
    else:
        return re.findall(r'[0-9-A-za-z]+', text)


def phone_number(text):
    phone_dict = {}
    split_list = re.findall(r'[0-9]+', text)
    if len(split_list) == 3:
        phone_dict['area_code'] = split_list[0]
        phone_dict['number'] = split_list[1] + '-' + split_list[2]
        return phone_dict
    elif len(split_list) == 2:
        return None
    elif len(split_list) == 1:
        for item in split_list:
            phone_dict['area_code'] = item[:3]
            phone_dict['number'] = item[3:6] + '-' + item[6:]
        return phone_dict


def money(dollars):
    symbol = re.search(r'^(?P<symbol>[$]{1})', dollars)
    if not symbol or len(dollars) == 1:
        return None
    number = re.search(r'(?P<number>^\$*[0-9]{1,3}?(\,?[0-9]{3})*(\.[0-9]{2})?$)', dollars)
    if(dollars[1] == '$' or not number):
        return None
    number = number[0][1:].replace(',', '')
    return {'currency': symbol[0], 'amount': float(number)}


def zipcode(number):
    result = re.search(r'^(?P<first>[0-9]{5})(-(?P<plus4>[0-9]{4}))?$', number)
    if result:
        return {"zip": result.group('first'), "plus4": result.group('plus4')}
    else:
        return None


def date(number):
    result = re.search(r'^(?P<slashes>(?P<s_month>[0-9]{1,2})[/](?P<s_day>[0-9]{1,2})[/](?P<s_year>[0-9]{4}))|(?P<hyphens>(?P<h_year>[0-9]{4})[-](?P<h_month>[0-9]{1,2})[-](?P<h_day>[0-9]{1,2}))', number)
    if result:
        if result.group('slashes'):
            return {"month": int(result.group('s_month')), "day": int(result.group('s_day')), "year": int(result.group('s_year'))}
        else:
            return {"month": int(result.group('h_month')), "day": int(result.group('h_day')), "year": int(result.group('h_year'))}
    return None
