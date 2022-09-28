import pytest

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.loginPage = LoginPage(self.driver)

    @pytest.mark.parametrize('username, password, message', [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("", "", "Epic sadface: Username is required")])
    def test_unsuccessful_login(self, username, password, message):
        self.loginPage.do_login(username, password)
        error = self.loginPage.get_error_message()
        assert error == message

    @pytest.mark.parametrize('username, password, message', TestData.extract_csv("..\Resources\data.csv"))
    def test_unsuccessful_login_csv(self, username, password, message):
        self.loginPage.do_login(username, password)
        error = self.loginPage.get_error_message()
        assert error == message
