from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.vklady_locators import VkladySelectors
from Tests.UI.Helpers.Endpoints import Endpoints

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

