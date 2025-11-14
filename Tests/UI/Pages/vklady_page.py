from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.vklady_locators import VkladySelectors
from Tests.UI.Helpers.Endpoints import Endpoints
"""
    Класс VkladyPage предназначен для взаимодействия со страницей вкладов в веб-приложении.
    Наследует базовые функции от BasePage и предоставляет методы для открытия страницы, заполнения формы,
    выбора различных фильтров и параметров вкладов, а также получения информации о выбранных элементах.
    
    Методы:
    - open(): открывает страницу вкладов по указанному эндпоинту.
    - fill_money(quantity): вводит сумму вклада в соответствующее поле.
    - choose_opening_method(opening_method_text): выбирает метод открытия вклада по тексту.
    - click_all_filters(text): активирует все фильтры по текстовому описанию.
    - click_checkbox_with_text(text): ставит галочку в чекбоксе по тексту.
    - choose_bank(text): выбирает банк из выпадающего списка.
    - choose_term(text): выбирает срок вклада.
    - click_show_button(text): нажимает кнопку для отображения результатов или подтверждения.
    - get_bank_name(text): возвращает элемент с названием банка.
    - get_terms(text): возвращает элемент с условиями или сроками вклада.
"""
class VkladyPage(BasePage):

    def open(self):
        self.open_page(Endpoints.VKLADY)

    def fill_money(self, quantity: str):
        self.click(VkladySelectors.INPUT_MONEY.value)
        self.type(VkladySelectors.INPUT_MONEY.value,quantity)

    def choose_opening_method(self, opening_method_text: str):
        self.click_by_selector_and_text(VkladySelectors.OPENING_METHOD_SELECTOR.value,opening_method_text,flag=True)

    def click_all_filters(self,text: str):
        self.click_by_selector_and_text(VkladySelectors.ALL_FILTERS.value, text, flag=True)

    def click_checkbox_with_text(self,text: str):
        self.click_by_selector_and_text(VkladySelectors.CHECKBOX_SELECTOR.value, text, flag=True)

    def choose_bank(self,text: str):
        self.click(VkladySelectors.DROPDOWN_MENU_BANKS)
        self.click_by_selector_and_text(VkladySelectors.DROPDOWN_SELECTOR.value,text, flag=True)
        
    def choose_term(self,text: str):
        self.click(VkladySelectors.CHOOSE_TERM)
        self.click_by_selector_and_text(VkladySelectors.DROPDOWN_SELECTOR.value,text, flag=True)

    def click_show_button(self,text: str):
        self.click_by_selector_and_text(VkladySelectors.SHOW_BUTTON_POPUP.value, text, flag=True)

    def get_bank_name(self,text: str):
         return self.get_element_by_selector_and_text(VkladySelectors.BANK_NAME.value , text,flag=True)

    def get_terms(self,text: str):
         return self.get_element_by_selector_and_text(VkladySelectors.TERMS.value , text,flag=True)

