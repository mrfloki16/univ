#!/bin/python3

from plates import is_valid

def test_begining():
  assert is_valid("2222") == False

def test_length():
  assert is_valid("AAA2222") == False 

def test_number_placement():
  assert is_valid("AA22AA") == False

def test_zero_placement():
  assert is_valid("AA022") == False

def test_alpha_num():
  assert is_valid("AA..22") == False
