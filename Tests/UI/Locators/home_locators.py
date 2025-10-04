from enum import Enum

class HomeSelectors(str, Enum):
    JSON_SERVER_BUTTON_XPATH = "//a[text()='{text}']"
    MENU_CREDIT_BUTTON = "a[data-label='{text}']"