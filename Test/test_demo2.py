import pytest


@pytest.mark.smoke
def test_firstProgrm():
    msg = "Hello"
    assert msg == "Hi", "Test Fail beacuse String dont match"

def test_secondCreditCard():
    a = 4
    b = 2
    assert a+2 == 6,"Addition do not match"


