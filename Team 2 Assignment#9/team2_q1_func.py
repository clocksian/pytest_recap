def calc_number_of_seconds(time_period, unit):
    if unit == 'second':
        return round(time_period, 2)

    if unit == 'minute':
        return round(time_period*60, 2)

    if unit == 'hour':
        return round(time_period*60*60, 2)

    if unit == 'day':
        return round(time_period*60*60*24, 2)

    if unit == 'week':
        return round(time_period*60*60*24*7, 2)
    
    if unit == 'month':
        return round(time_period*60*60*24*30, 2)

    if unit == 'year':
        return round(time_period*365*12*30*24*60*60, 2)

    else:
        raise Exception