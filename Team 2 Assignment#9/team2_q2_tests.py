import pytest
from team2_q2_func import *

# pound to kilogram
def test_lb_kg():
    assert convert_units(4, 'pound', 'kilogram') == 1.8

# kilogram to pound
def test_kg_lb():
    assert convert_units(4, 'kilogram', 'pound') == 8.89

# mile to kilometer
def test_mile_km():
    assert convert_units(2, 'mile', 'kilometer') == 3.22

# kilometer to mile
def test_km_mile():
    assert convert_units(2, 'kilometer', 'mile') == 1.24

# fahrenheit to celsius 
def test_F_C():
    assert convert_units(32, 'fahrenheit', 'celsius') == 0

# celsius to fahrenheit 
def test_C_F():
    assert convert_units(100, 'celsius', 'fahrenheit') == 212

# gallon to liter
def test_gallon_liter():
    assert convert_units(1, 'gallon', 'liter') == 3.79

# liter to gallon
def test_liter_gallon():
    assert convert_units(1, 'liter', 'gallon') == 0.26

# test wrong units or conversion
# the conversion is not defined here
@pytest.mark.xfail
def test_pound_gram():
    assert convert_units(1, 'pound', 'gram') == 453.59

# the conversion cannot match
def test_liter_mile():
    assert convert_units(1, 'liter', 'mile') == None
