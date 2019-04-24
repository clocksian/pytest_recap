

def calc_number_of_seconds(time_period, unit):

    units = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']

    if unit not in units:
        raise Exception

    if unit =='year':

        second = time_period * 365 *24 * 60 * 60
        return second

    elif unit == 'month':

        second = time_period * 30 * 24 * 60 * 60
        return second

    elif unit == 'week':

        second = time_period * 7 * 24 * 60 * 60
        return second

    elif unit == 'day':

        second = time_period * 24 * 60 * 60
        return second

    elif unit == 'hour':

        second = time_period * 60 * 60
        return second

    elif unit == 'minute':

        second = time_period * 60
        return second

    return time_period






