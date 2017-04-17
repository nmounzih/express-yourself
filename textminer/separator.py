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
    result = re.search(r'^(?P<symbol>[$]{1})'
                        r'(?P<number>^\$[0-9]{1,3}?(\,?[0-9]{3})*(\.[0-9]{2})?$', dollars)
    if result:
        return {'currency': result.group('symbol'), 'amount': result.group('number')}
    return None
    # money_dict = {}
    # match = re.findall(r'(?P<sign>[$]{1})(?P<how_much>[\d]+)', number)
    # for item in match:
    #     money_dict['currency'] = item[0]
    #     money_dict['amount'] = item[1]
    # return money_dict


def zipcode(number):
    result = re.search(r'^(?P<main>[0-9]{5})'
                        r'[-](?P<four>(?:-[0-9]{4})?$', number)
    if result:
        retun {'zip': result.group('original'), 'plus4': result.group('four')}
    return None


def date(number):
     result = re.search(r'(?P<forward>(?P<my_month>([\d]{1,2}[/]))'
                       r'(?P<my_day>([\d]{1,2}[/]))(?P<my_year>[\d]{4}))'
                       r'|(?P<rev_year>[\d]{4})(?P<rev_month>([-][\d]{2}))'
                       r'(?P<rev_day>([-][\d]{2}))', number)
    if result:
        if result.group('forward'):
            return {'month': int(re.sub('^[0]', '',
                                        re.sub('[/]', '',
                                               result.group('my_month')))),
                    'day': int(re.sub('^[0]', '',
                                      re.sub('[/]', '',
                                             result.group('my_day')))),
                    'year': int(result.group('my_year'))}
        return {'month': int(re.sub('^[0]', '',
                                    re.sub('[-]', '',
                                           result.group('rev_month')))),
                'day': int(re.sub('^[0]', '',
                                  re.sub('[-]', '',
                                         result.group('rev_day')))),
                'year': int(result.group('rev_year'))}
    return None
