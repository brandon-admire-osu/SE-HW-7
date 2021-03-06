from "./fizzbuzz.py" import *

def test_three_case():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(6) == "Fizz"
    assert fizzBuzz(9) == "Fizz"

def test_five_case():
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(10) == "Buzz"
    assert fizzBuzz(20) == "Buzz"

def test_three_and_five_case():
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(30) == "FizzBuzz"
    assert fizzBuzz(45) == "FizzBuzz"

def test_default_case():
    assert fizzBuzz(1) == 1
    assert fizzBuzz(2) == 2
    assert fizzBuzz(4) == 4
    assert fizzBuzz(7) == 7
