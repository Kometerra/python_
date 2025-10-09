from enum import Enum

class MicrozaimSelectors(str, Enum):
    MONEY_SLIDER = 'div[class*=SliderInput_module_slider] [class*=Slider_module_inner]'
    TERM_SLIDER = 'div[class*=FullDealTermSlider_slider] [class*=Slider_module_inner]'