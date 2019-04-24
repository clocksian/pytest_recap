import pytest 
from team2_q1_func import *


def test_sec_to_sec():
    assert calc_number_of_seconds(1, 'second') == 1

def test_min_to_sec():
    assert calc_number_of_seconds(1, 'minute') == 60

def test_hour_to_sec():
    assert calc_number_of_seconds(1, 'hour') == 60*60

def test_day_to_sec():
    assert calc_number_of_seconds(1, 'day') == 24*60*60

def test_week_to_sec():
    assert calc_number_of_seconds(1, 'week') == 7*24*60*60

def test_month_to_sec():
    assert calc_number_of_seconds(1, 'month') == 30*24*60*60

def test_year_to_sec():
    assert calc_number_of_seconds(1, 'year') == 365*12*30*24*60*60

def test_wrong_unit():
    with pytest.raises(Exception):
        calc_number_of_seconds(2, 'months')