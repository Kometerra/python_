from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.home_locators import HomeSelectors
from Tests.UI.Helpers.Endpoints import Endpoints

class HomePage(BasePage):
    def open(self):
        self.open_page(Endpoints.HOME)

    def click_button(self, text: str = "JSON Server"):
        xpath = HomeSelectors.JSON_SERVER_BUTTON_XPATH.format(text=text)
        self.click(xpath)

    def get_json_server_button(self, text: str = "JSON Server"):
        xpath = HomeSelectors.JSON_SERVER_BUTTON_XPATH.format(text=text)
        return self.find(xpath)

    def get_menu_credit_button(self,text:str):
        css = HomeSelectors.MENU_CREDIT_BUTTON.format(text=text)
        return self.find(css)

    def click_menu_button(self, text: str):
        css = HomeSelectors.MENU_CREDIT_BUTTON.format(text=text)
        self.click(css)

