#!/bin/python3

from twttr import shorten

def test_upper_case():
  assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_lower_case():
  assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_ponctuation():
  assert shorten("twitter, good") == "twttr, gd"

def test_number():
  assert shorten("twitter#1") == "twttr#1"

if __name__ == "__main__":
  main()
