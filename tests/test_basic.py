import src.calculs.basic as ba
import pytest

def test_add_positive():
    assert ba.add(1, 2) == 3

def test_add_negative():
    assert ba.add(-1, -1) == -2

def test_add_zero():
    assert ba.add(0, 5) == 5

def test_mul_positive():
    assert ba.mul(2, 3) == 6

def test_mul_negative():
    assert ba.mul(-2, 3) == -6

def test_mul_zero():
    assert ba.mul(0, 100) == 0