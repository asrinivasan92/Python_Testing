import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def editprofile(self, dataLoad):
        print(dataLoad)