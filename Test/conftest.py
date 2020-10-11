import pytest
from selenium import webdriver


@pytest.fixture()

def Invoke(request):
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

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
