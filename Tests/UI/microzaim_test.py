import pytest
from Tests.UI.Helpers.Assertions import UIAssertions
from Pages.microzaim_page import MicrozaimPage

@pytest.mark.microzaim
def test_get_microzaim(page, get_base_url_ui):
    microzaim_page = MicrozaimPage(page, get_base_url_ui)
    microzaim_page.open()
    microzaim_page.click_money_with_coordinates(52000)
    page.wait_for_timeout(3000)
    microzaim_page.click_term_with_coordinates(30)
    page.wait_for_timeout(3000)