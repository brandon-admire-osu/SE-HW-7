from "./leapyear.py" import *

def test_4_divide():
    assert leap_check(8)
    assert leap_check(12)
    assert leap_check(16)

def test_100_divide():
    assert not leap_check(100)
    assert not leap_check(200)
    assert not leap_check(300)

def test_400_divide():
    assert leap_check(400)
    assert leap_check(800)
    assert leap_check(1200)

def test_default():
    assert not leap_check(1)
    assert not leap_check(2)
    assert not leap_check(3)