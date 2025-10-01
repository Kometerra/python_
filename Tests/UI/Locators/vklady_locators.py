from enum import Enum

class VkladySelectors(str, Enum):
    INPUT_MONEY = 'div[data-qa="Dialog"] input[inputmode="decimal"]'
    OPENING_METHOD_SELECTOR = 'label[data-qa="Radio"] span'
    ALL_FILTERS = '[class*="DepositFilters_button"]'
    CHECKBOX_SELECTOR = 'label[data-qa="Checkbox"] span'
    DROPDOWN_MENU_BANKS = 'div[data-qa="Dialog"] div[data-qa="Autocomplete"]'
    DROPDOWN_SELECTOR = 'div[data-qa="Dropdown"] div[data-qa="Space"] div[data-qa="Space"] div'
    CHOOSE_TERM = 'div[data-qa="Dialog"] div[data-qa="Select"]'
    SHOW_BUTTON_POPUP = 'div[data-qa="Dialog"] button[data-qa="Button"] span'
    BANK_NAME = '[class*="DepositCard_title"]'
    TERMS = '[class*="CardColumn_title"]'