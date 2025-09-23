import pytest
from Pages.home_page import HomePage
from Tests.UI.Helpers.Assertions import UIAssertions

@pytest.mark.ui
def test_menu_credit_button(page, get_base_url_ui):
    some_page = HomePage(page, get_base_url_ui)
    some_page.open()

    button = some_page.get_menu_credit_button()
    UIAssertions.assert_element_visible(button)
    