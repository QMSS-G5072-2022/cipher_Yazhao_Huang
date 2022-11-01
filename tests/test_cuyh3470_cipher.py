from cuyh3470_cipher import cipher
import pytest


def test_cipher_a():
    example = 'Lisa'
    expected = 'Mjtb'
    actual = cipher(example, 1)
    assert actual == expected
    