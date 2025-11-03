from Tests.UI.Pages.base_page import BasePage
from Tests.UI.Locators.insurance_locators import InsuranceSelectors
from Tests.UI.Helpers.Endpoints import Endpoints
from Tests.UI.Helpers.DateHelper import DateHelper
import logging

class InsurancePage(BasePage):
    def open(self):
        self.open_page(Endpoints.INSURANCE)

    def click_destination_input(self):
        self.click(InsuranceSelectors.DESTINATION)

    def input_country(self,text:str):
        self.click(InsuranceSelectors.INPUT_COUNTRY)
        self.type(InsuranceSelectors.INPUT_COUNTRY,text)

    def select_country(self,text: str):
        css = InsuranceSelectors.CHECKBOX_COUNTRY.format(text=text)
        self.click(css)

    def click_continue(self, text:str):
        xpath = InsuranceSelectors.BUTTON_CONTINUE.format(text=text)
        self.click(xpath)

    def input_age(self, text: str):
        self.click(InsuranceSelectors.AGE)
        self.type(InsuranceSelectors.AGE_INPUT, text)

    def input_date(self, offset_days: int):
        day = DateHelper.generate_day_after_offset(offset_days)
        index = DateHelper.get_index_for_calendar_click(day)
        self.click_by_selector_and_text_and_index(InsuranceSelectors.CALENDAR_DAY.value, day, index)
        logging.info(day)
        logging.info(index)

    def open_calendar(self):
        self.click(InsuranceSelectors.DATE_INPUT)

    def submit_insurance(self):
        self.click(InsuranceSelectors.SUBMIT_BUTTON)

    def get_insurance(self):
         return self.find(InsuranceSelectors.INSURANCE_OFFERS)