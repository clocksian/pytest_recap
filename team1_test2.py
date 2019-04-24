import pytest
from team1_q2 import *

# Units Matching
@pytest.mark.xfail
def test_pound_kilometer():
    assert convert_units(4, 'pound', 'kilometer')

@pytest.mark.xfail
def test_pound_gallon():
    assert convert_units(4, 'pound', 'gallon')

# Units Not Allowed
@pytest.mark.xfail
def test_kelvin_celsius():
    assert convert_units(273, 'kevlin', 'celsius')

@pytest.mark.xfail
def test_mph_kph():
    assert convert_units(360, 'mph', 'kph')

# Pound to Kilogram
def test_p2k():
    assert convert_units(4, 'pound', 'kilogram') == 1.8

# Kilogram to Pound
def test_k2p():
    assert convert_units(1.8, 'kilogram', 'pound') == 4

# Mile to Kilometer
def test_m2k():
    assert convert_units(1.24, 'mile', 'kilometer') == 2

# Kilometer to Mile
def test_k2m():
    assert convert_units(2, 'kilometer', 'mile') == 1.24

# Fahrenheit to Celsius
def test_f2c():
    assert convert_units(77, 'fahrenheit', 'celsius') == 25

# Celsius to Fahrenheit
def test_c2f():
    assert convert_units(25, 'celsius', 'fahrenheit') == 77

# Gallon to Liter
def test_g2l():
    assert convert_units(16, 'gallon', 'liter') == 60.64

# Liter to Gallon
def test_l2g():
    assert convert_units(60.64, 'liter', 'gallon') == 16