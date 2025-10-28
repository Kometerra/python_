from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.mfo_locators import MfoSelectors
from Tests.UI.Helpers.Endpoints import Endpoints

class MfoPage(BasePage):
    def get_elements_with_terms(self):
        return self.find(str(MfoSelectors.POP_UP_TERMS))

    def open(self):
        self.open_page(Endpoints.MFO_POPUP)