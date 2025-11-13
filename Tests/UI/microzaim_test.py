import pytest
from Tests.UI.Helpers.Assertions import UIAssertions
from Tests.UI.Pages.microzaim_page import MicrozaimPage

@pytest.mark.ui
@pytest.mark.microzaim
def test_get_microzaim(page, get_base_url_ui):
    microzaim_page = MicrozaimPage(page, get_base_url_ui)
    microzaim_page.open()
    microzaim_page.click_money_with_coordinates(52000)
    microzaim_page.click_term_with_coordinates(20)
    microzaim_page.click_get_zaim("Получить деньги")
    microzaim_page.reload()
    zaim_term_popup = microzaim_page.get_popup_term()

    UIAssertions.assert_element_visible(zaim_term_popup)

