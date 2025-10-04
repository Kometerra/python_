import pytest
from Tests.UI.Helpers.Assertions import UIAssertions
from Pages.vklady_page import VkladyPage

@pytest.mark.vklady
def test_filter_vklady(page, get_base_url_ui):
    vklady_page = VkladyPage(page, get_base_url_ui)
    vklady_page.open()

    vklady_page.click_all_filters("Все фильтры")
    vklady_page.fill_money('600000')
    vklady_page.choose_opening_method("Онлайн")
    vklady_page.click_checkbox_with_text("Частичное снятие")
    vklady_page.click_checkbox_with_text("Регулярно")
    vklady_page.choose_bank("Банк Уралсиб")
    vklady_page.choose_term("1 месяц")
    vklady_page.click_show_button("Показать")
    bank_name = vklady_page.get_bank_name("Банк Уралсиб")
    UIAssertions.assert_element_visible(bank_name)
    terms = vklady_page.get_terms("Заработаете за 1 мес")
    UIAssertions.assert_element_visible(terms)
