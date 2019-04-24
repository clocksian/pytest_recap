def convert_units(amount, current_unit, converted_unit):
    units = {
        'pound' : 'kilogram',
        'kilogram' : 'pound',
        'mile' : 'kilometer',
        'kilometer' : 'mile',
        'fahrenheit' : 'celsius',
        'celsius' : 'fahrenheit',
        'gallon' : 'liter',
        'liter' : 'gallon'
    }
    if current_unit in units:
        if units[current_unit] == converted_unit:
            pass
        else:
            raise ValueError('The units do not match.')
    else:
        raise ValueError('The units are not allowed.')

    converted_amount = 0
    if current_unit == 'pound':
        converted_amount = amount*.45
    elif current_unit == 'kilogram':
        converted_amount = amount/.45
    elif current_unit == 'mile':
        converted_amount = amount*1.61
    elif current_unit == 'kilometer':
        converted_amount = amount/1.61
    elif current_unit == 'fahrenheit':
        converted_amount = 5/9*(amount-32)
    elif current_unit == 'celsius':
        converted_amount = amount*9/5+32
    elif current_unit == 'gallon':
        converted_amount = amount*3.79
    else:
        converted_amount = amount/3.79

    return round(converted_amount, 2)