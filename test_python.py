import math


def test_filter():
    text = (2, 4, 5, 678, 3, 24, 54, 3, 345)
    assert list(filter(lambda n: n > 20, text)) == [678, 24, 54, 345]


def test_map():
    numbers = [1, 2, 3, 4, 5]
    assert list(map(lambda n: n * 5, numbers)) == [5, 10, 15, 20, 25]


def test_sorted():
    s2 = "hello"
    assert list(sorted(s2)) == ['e', 'h', 'l', 'l', 'o']


def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(9) == 3


def test_pow():
    assert math.pow(5, 2) == 25


def test_hypot():
    assert math.hypot(3, 4) == 5
