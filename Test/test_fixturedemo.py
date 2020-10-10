import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
       print("I will execute step fixture demo")

    def test_fixtureDemo1(self):
       print("I will execute step fixture demo")

    def test_fixtureDemo2(self):
       print("I will execute step fixture demo")



