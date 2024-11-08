#!/home/mr_floki/py_venv/bin/python3

import pytest
from fuel import convert, gauge

def test_convert():
  assert convert("1/4") == 25
  assert convert("1/2") == 50

def test_gauge():
  assert gauge(1) == "E"
  assert gauge(25) == "25%" 
  assert gauge(99) == "F"

def test_value_error():
  with pytest.raises(ValueError):
    convert("1.4/1.5")

def test_zero_division():
  with pytest.raises(ZeroDivisionError):
    convert("1/0")
