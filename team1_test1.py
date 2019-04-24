from team1_q1 import *
import team1_q1
import pytest

def test_year():

    assert calc_number_of_seconds(1, 'year')  == 31536000


def test_month():

    assert calc_number_of_seconds(1, 'month') == 2592000


def test_week():

    assert calc_number_of_seconds(1, 'week') == 604800

def test_day():

    assert calc_number_of_seconds(1, 'day') ==  86400


def test_hour():

    assert calc_number_of_seconds(1, 'hour') == 3600

def test_minute():


    assert calc_number_of_seconds(1, 'minute') == 60

def test_second():

    assert calc_number_of_seconds(1, 'second') == 1

def units_is_wrong():
    with pytest.raises(Exception):
        calc_number_of_seconds(1, 'seconds')
