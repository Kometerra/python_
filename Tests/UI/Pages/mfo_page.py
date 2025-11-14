from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.mfo_locators import MfoSelectors
from Tests.UI.Helpers.Endpoints import Endpoints
"""
    Класс MfoPage предназначен для взаимодействия с страницей МФО (микрофинансовой организации) в веб-приложении.
    Наследует от BasePage и предоставляет методы для открытия страницы и получения элементов, связанных с условиями или соглашениями (например, всплывающие окна с условиями).
    
    Методы:
    - open(): открывает страницу МФО по заданному эндпоинту.
    - get_elements_with_terms(): ищет и возвращает элементы, связанные с условиями или соглашениями, используя локатор POP_UP_TERMS.
"""
class MfoPage(BasePage):
    def get_elements_with_terms(self):
        return self.find(str(MfoSelectors.POP_UP_TERMS))

    def open(self):
        self.open_page(Endpoints.MFO_POPUP)