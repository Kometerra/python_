from Tests.UI.Pages.base_page import BasePage

class HomePage(BasePage):
    JSON_SERVER_BUTTON_XPATH = "//a[text()='{text}']"
    ENDPOINT='/'
    MENU_CREDIT_BUTTON = "a[data-label='{text}']"

    def open(self):
        self.open_page(self.ENDPOINT)

    def click_button(self, text: str = "JSON Server"):
        xpath = self.JSON_SERVER_BUTTON_XPATH.format(text=text)
        self.click(xpath)

    def get_json_server_button(self, text: str = "JSON Server"):
        xpath = self.JSON_SERVER_BUTTON_XPATH.format(text=text)
        return self.find(xpath)

    def get_menu_credit_button(self,text:str):
        css = self.MENU_CREDIT_BUTTON.format(text=text)
        return self.find(css)

    def click_menu_button(self, text: str):
        css = self.MENU_CREDIT_BUTTON.format(text=text)
        self.click(css)