import math as m
import pytest


def funck(a, b):
    try:
        y = m.sqrt(((a+b)**3)/((a-b)**2))
    except ZeroDivisionError:
        result = 'there is zero divizion'
        raise ZeroDivisionError
    except ValueError:
        result = "can't divide zero without complex"
    except TypeError:
        result = 'this is not a number'
    else:
        result = round(y,4)
    return result

# тестируемая часть приложения
def test_pos_int_difff():
    assert funck(1,2) == 5.1962

def test_integer_negative_numbers():
    assert funck(2,-1) == 0.3333

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert funck(2,2) in str(er.value)

def test_positive_numbers():
    assert funck(0.2, 0.1) == 1.6432

def test_negative_root():
    assert funck(1, -2) == "can't divide zero without complex"

def test_error_input():
    assert funck('asdff', 0) == 'this is not a number'
    assert funck('', 0) ==  'this is not a number'
    assert funck('10**-9', 0) == 'this is not a number'
