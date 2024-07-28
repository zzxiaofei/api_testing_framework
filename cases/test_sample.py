import pytest


def test_sample(x):
    return x + 1


def test_answer():
    assert test_sample(3) == 5


def test_success():
    assert test_sample(4) == 5


if __name__ == '__main__':
    pytest.main(['-s', 'test_sample.py'])
