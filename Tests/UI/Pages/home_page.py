from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.home_locators import HomeSelectors
from Tests.UI.Helpers.Endpoints import Endpoints
"""
    Класс HomePage представляет собой страницу главной панели веб-приложения,
    предоставляя методы для взаимодействия с элементами интерфейса, такими как кнопки и меню.
    Наследует базовую функциональность из класса BasePage, обеспечивая автоматизированное
    открытие страницы, поиск элементов, клики и получение элементов по селекторам.
    
    Методы:
    - open(): открывает страницу главной панели по заданной конечной точке.
    - click_button(text): кликает по кнопке с указанным текстом.
    - get_json_server_button(text): возвращает локатор кнопки с указанным текстом.
    - get_menu_credit_button(text): возвращает локатор элемента меню по тексту.
    - click_menu_button(text): кликает на элемент меню по тексту.
"""
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

