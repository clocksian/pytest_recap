def convert_units(amount, current_unit, converted_unit):
    if current_unit == 'pound':
        if converted_unit == 'kilogram':
            return round(amount*0.45, 2)
    
    if current_unit == 'kilogram':
        if converted_unit == 'pound':
            return round(amount/0.45, 2)

    if current_unit == 'mile':
        if converted_unit == 'kilometer':
            return round(amount*1.61, 2)

    if current_unit == 'kilometer':
        if converted_unit == 'mile':
            return round((amount / 1.61),2)

    if current_unit == 'fahrenheit':
        if converted_unit == 'celsius':
            return round(5/9*(amount-32), 2) 

    if current_unit == 'celsius': 
        if converted_unit == 'fahrenheit':
            return round(9/5*amount +32, 2)

    if current_unit == 'gallon':
        if converted_unit == 'liter':
            return round(amount*3.79, 2)

    if current_unit == 'liter':
        if converted_unit == 'gallon':
            return round(amount/3.79, 2)

    else: 
        raise ValueError('The units are wrong or not allowed here.')
    
    