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
        term = term/8/100
        self.click_coordinates(MicrozaimSelectors.TERM_SLIDER, term)
