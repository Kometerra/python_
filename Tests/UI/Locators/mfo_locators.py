from enum import Enum

class MfoSelectors(str, Enum):
    POP_UP_TERMS = "div[data-qa='Card'] div[class*='Text_module_size14']"