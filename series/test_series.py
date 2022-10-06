import pytest
from series import fibonacci
from series import lucas


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected



