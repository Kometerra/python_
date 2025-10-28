from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.microzaim_locators import MicrozaimSelectors
from Tests.UI.Helpers.Endpoints import Endpoints

class MicrozaimPage(BasePage):

    def open(self):
        self.open_page(Endpoints.MICROZAIM)

    def click_money_with_coordinates(self, money):
        money = (money-1000)/100000  # вычитаем 1000 руб для приведения к нужной сумме
        self.click_coordinates(MicrozaimSelectors.MONEY_SLIDER,money)

    def click_term_with_coordinates(self, term):
        term = (term - 10)//2/7 # Сначала делим на 2, чтобы получить недели, затем делим на 7, чтобы получить процент
        self.click_coordinates(MicrozaimSelectors.TERM_SLIDER, term)

    def click_get_zaim(self,text: str):
        xpath = MicrozaimSelectors.BUTTON_WITH_TEXT.format(text=text)
        self.click(xpath)

    def get_popup_term(self):
        return self.find(MicrozaimSelectors.POP_UP)