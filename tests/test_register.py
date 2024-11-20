import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Arun", "Motoori", self.generate_email_with_timestamp(), "123456789", "123456", "123456","no","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    @pytest.mark.parametrize("name, lastname, telephone, password, confirmpass, yes_or_no, select", ExcelUtils.get_data_from_excel("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest"))
    def test_register_with_all_fields(self, name, lastname, telephone, password, confirmpass, yes_or_no, select):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(name, lastname, self.generate_email_with_timestamp(), telephone, password, confirmpass, yes_or_no, select)
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Arun", "Motoori",
                                                                 "andriypolik@ukr.net", "123456789",
                                                                 "123456", "123456", "yes", "select")

        expected_warning_email_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_email_text)


    def test_register_without_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "")

        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!","First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!","E-Mail Address does not appear to be valid!","Telephone must be between 3 and 32 characters!","Password must be between 4 and 20 characters!")