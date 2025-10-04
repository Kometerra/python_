class BasePage:
    """
    Базовые методы для работы с UI.

    Методы позволяют открывать страницу, находить элементы на странице
    кликать на элемент, заполнять, находить текст.
    """

    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open_page(self, endpoint: str = ""):
        """
        Открывает страницу.

        :param endpoint: эндпоинт к base url
        """
        full_url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        self.page.goto(full_url)


    def find(self, selector: str):
        return self.page.locator(selector)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def type(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        return self.page.locator(selector).inner_text()

    def click_by_selector_and_text(self,selector: str,text: str, flag: bool):
        self.page.locator(selector).get_by_text(text,exact=flag).click()

    def get_element_by_selector_and_text(self,selector: str,text: str, flag: bool):
        return self.page.locator(selector).get_by_text(text,exact=flag)


