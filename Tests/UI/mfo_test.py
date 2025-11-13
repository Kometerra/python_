import pytest
from Tests.UI.Helpers.Assertions import UIAssertions
from Tests.UI.Pages.mfo_page import MfoPage

@pytest.mark.ui
@pytest.mark.mfo
def test_check_mfo_terms(page, get_base_url_ui):
    mfo_page = MfoPage(page, get_base_url_ui)
    mfo_page.open()

    elements = mfo_page.get_elements_with_terms()
    expected_texts = [
        "Чтобы заполнить анкету и узнать персональные условия по займу",
        "Оформление за 5 минут",
        "Высокая вероятность одобрения",
        "Без скрытых условий"
    ]

    UIAssertions.assert_check_many_texts(elements, expected_texts)