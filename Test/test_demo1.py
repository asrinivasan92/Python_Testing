import pytest


def test_firstprogram(setup):
    print("Hello")

@pytest.mark.smoke
def test_Secondtprogram():
    print("Good Morning")

def test_crossbrowser(crossbrowser):
    print(crossbrowser)