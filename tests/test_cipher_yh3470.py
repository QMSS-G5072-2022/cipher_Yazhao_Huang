from cipher_Yazhao_Huang import cipher_yh3470
import pytest

def test_cipher_a():
    example = 'Lisa'
    expected = 'Mjtb'
    actual = cipher(example, 1)
    assert actual == expected
    