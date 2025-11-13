import pytest
from Tests.UI.Helpers.Assertions import UIAssertions
from Tests.UI.Pages.insurance_page import InsurancePage

@pytest.mark.ui
@pytest.mark.insurance
def test_select_insurance(page, get_base_url_ui):
    """
    Открываем страницу туристической страховки
    """
    insurance_page = InsurancePage(page, get_base_url_ui)
    insurance_page.open()
    """
      Заполняем страну посещения
      """
    insurance_page.click_destination_input()
    insurance_page.input_country("Таиланд")
    insurance_page.select_country("Таиланд")
    insurance_page.click_continue("Продолжить")
    """
      Заполняем возраст
      """
    insurance_page.input_age("28")
    """
      Выбираем даты посещения страны
      """
    insurance_page.open_calendar()
    insurance_page.input_date(5)
    insurance_page.input_date(28)
    insurance_page.open_calendar()
    """
      Подтверждаем выбранные критерии
      """
    insurance_page.submit_insurance()
    """
      Проверяем отображение вариантов страховых предложений
      """
    insurance = insurance_page.get_insurance()
    UIAssertions.assert_element_visible(insurance)