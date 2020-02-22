#!/usr/bin/env python


def minus(a, b):
    return a-b


def test_basic_found():
    a = 2
    b = 1
    expected = 1
    actual = minus(a, b)
    assert actual == expected
