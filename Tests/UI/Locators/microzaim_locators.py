from enum import Enum

class MicrozaimSelectors(str, Enum):
    MONEY_SLIDER = 'div[class*=SliderInput_module_slider] [class*=Slider_module_inner]'
    TERM_SLIDER = 'div[class*=FullDealTermSlider_slider] [class*=Slider_module_inner]'
    BUTTON_WITH_TEXT ='//span[contains(@class,"Button_module_text")][text()="{text}"]/parent::button'
    POP_UP = 'div[data-qa="Dialog"]'