#!/usr/bin/env python


def add(a, b):
    return a+b


def test_basic_found():
    a = 1
    b = 2
    expected = 3
    actual = add(a, b)
    assert actual == expected
