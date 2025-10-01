class UIAssertions:
    @staticmethod
    def assert_text_equals(element, expected_text: str):
        actual_text = element.text
        assert actual_text == expected_text, (
            f'Ожидался текст: "{expected_text}", но получен: "{actual_text}"'
        )

    @staticmethod
    def assert_element_visible(element,timeout: int=5000):
        element.wait_for(state="visible", timeout=timeout)
        assert element.is_visible(), "Элемент не отображается на странице"

    @staticmethod
    def assert_url_contains(page, expected_part: str):
        current_url = page.url
        assert expected_part in current_url, f"Ожидали, что URL содержит '{expected_part}', но получили '{current_url}'"

    @staticmethod
    def assert_title_is(driver, expected_title: str):
        actual_title = driver.title
        assert actual_title == expected_title, (
            f'Ожидался заголовок: "{expected_title}", но получен: "{actual_title}"'
        )