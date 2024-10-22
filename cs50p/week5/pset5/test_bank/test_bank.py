#!/bin/python3

from bank import value

def test_incorrect_value():
  assert value("hello") == 0

def test_case_sensitive():
  assert value("Hey") == 20

def test_phrase():
  assert value("What's happening?") == 100
