from enum import Enum

class InsuranceSelectors(str, Enum):
    DESTINATION = "div[data-qa='Select'] div[data-qa='TextInput']"
    INPUT_COUNTRY = "div[data-qa='Dialog'] input[id*='textInput']"
    CHECKBOX_COUNTRY = "div[data-qa='Space'][label='{text}']"
    BUTTON_CONTINUE = "//div[text()='Продолжить']"
    AGE = "div[class*='FormFields_secondary-input-white-age'] div[data-qa='TextInput']"
    AGE_INPUT= "div[data-qa='NumberInput'] input"
    DATE_INPUT = "div[class*='FormFields_secondary-input-white-date'] div[data-qa='TextInput']"
    CALENDAR_DAY = "div[class*='CalendarDay_calendar-day'] div"
    SUBMIT_BUTTON = "button[type='submit'] span"
    INSURANCE_OFFERS= "div[class*='BaseLayout_container'] div[class*='PropositionCard_recommended']"