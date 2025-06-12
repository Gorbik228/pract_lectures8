import math as m
import pytest
import funk as f

# тестируемая часть приложения
def test_pos_int_difff():
    assert f.funck(1,2) == 5.1962

def test_integer_negative_numbers():
    assert f.funck(2,-1) == 0.3333

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert f.funck(2,2) in str(er.value)

def test_positive_numbers():
    assert f.funck(0.2, 0.1) == 1.6432

def test_negative_root():
    assert f.funck(1, -2) == "can't divide zero without complex"

def test_error_input():
    assert f.funck('asdff', 0) == 'this is not a number'
    assert f.funck('', 0) ==  'this is not a number'
    assert f.funck('10**-9', 0) == 'this is not a number'
