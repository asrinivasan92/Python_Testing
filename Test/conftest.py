import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    print("I will be Executing First")
    yield
    print("Quit")

@pytest.fixture()
def dataLoad():
    print("User data is bee created")
    return ["Ashok", "Srinivasan","byte.com"]

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossbrowser(request):
     return request.param
