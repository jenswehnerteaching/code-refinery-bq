import pytest
def add(a,b):
  return a + b

def test_add():
  assert add(1,2)==3
  
def subtract(a,b):
  return a - b

def product(a,b):
  return a * b
