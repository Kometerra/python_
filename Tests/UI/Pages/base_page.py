from asyncio import timeout

from playwright.sync_api import expect, TimeoutError, Error


class BasePage:
    """
    Базовые методы для работы с UI.

    Методы позволяют открывать страницу, находить элементы на странице
    кликать на элемент, заполнять, находить текст.
    """

    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.timeout = timeout
        
    def open_page(self, endpoint: str = ""):
        """
        Открывает страницу.

        :param endpoint: эндпоинт к base url
        :raises AssertionError: если страница не открылось в установленное время или произошла ошибка.
        """

        full_url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            self.page.goto(full_url)
            expect(self.page).to_have_url(full_url, timeout=self.timeout)
        except TimeoutError:
            raise AssertionError(f'Страница не открылась: {full_url}')
        except Error as e:
            raise AssertionError(f'Ошибка при переходе на страницу {full_url}: {str(e)}')


    def find(self, selector: str):
        """
            Находит элемент по селектору и ожидает его видимости.

            :param selector: селектор элемента.
            :return: Локатор элемента для дальнейших действий.
            :raises AssertionError: если элемент не найден или не виден в течение таймаута или при ошибке.
        """
       try:
           locator = self.page.locator(selector)
           expect(locator).to_be_visible(timeout=self.timeout)
           return locator
       except TimeoutError:
           raise AssertionError(f'Элемент не найден или не виден {selector}')
       except Error as e:
           raise AssertionError(f'Ошибка при поиске элемента {selector}: {str(e)}')



    def click(self, selector: str):
        """
            Находит и кликает по элементу.

            :param selector: селектор элемента.
            :raises AssertionError: если элемент не кликабелен или произошла ошибка.
        """
       try:
           locator = self.find(selector)
           locator.click(timeout=self.timeout)
       except TimeoutError:
           raise AssertionError(f'Элемент не кликабелен {selector}')
       except Error as e:
           raise AssertionError(f'Ошибка при клике на элемент {selector}: {str(e)}')


    def type(self, selector: str, text: str):
        """
            Находит элемент и заполняет его текстом.

            :param selector: селектор элемента.
            :param text: Текст для ввода.
            :raises AssertionError: если невозможно заполнить элемент или произошла ошибка.
        """
        try:
            locator = self.find(selector)
            locator.fill(text, timeout=self.timeout)
        except TimeoutError:
            raise AssertionError(f'Невозможно ввести текст в элемент {selector}')
        except Error as e:
            raise AssertionError(f'Ошибка при вводе текста в элемент {selector}: {str(e)}')


    def get_text(self, selector: str):
        """
            Получает внутренний текст элемента.

            :param selector: селектор элемента.
            :return: Текст внутри элемента.
            :raises AssertionError: если невозможно получить текст или произошла ошибка.
         """
        try:
            locator = self.find(selector)
            return locator.inner_text(timeout=self.timeout)
        except TimeoutError:
            raise AssertionError(f'Невозможно получить текст из элемента {selector}')
        except Error as e:
            raise AssertionError(f'Ошибка при получении текста из элемента {selector}: {str(e)}')


    def click_by_selector_and_text(self,selector: str,text: str, flag: bool):
        """
            Находит подэлемент по тексту внутри выбранного селектора и кликает по нему.

            :param selector: селектор контейнера.
            :param text: Текст, по которому ищется элемент.
            :param flag: Флаг точного совпадения текста.
            :raises AssertionError: если элемент с текстом не найден или не кликабелен, или произошла ошибка.
        """
        try:
            locator = self.find(selector)
            target = locator.get_by_text(text,exact=flag)
            expect(target).to_be_visible(timeout=self.timeout)
            target.click()
        except TimeoutError:
            raise AssertionError(f'Элемент с текстом {text} не найден или не кликабелен внутри {selector}')
        except Error as e:
            raise AssertionError(f'Ошибка при клике по тексту {text} {selector}: {str(e)}')


    def get_element_by_selector_and_text(self,selector: str,text: str, flag: bool):
        """
            Находит элемент по селектору и тексту внутри него и возвращает его.

            :param selector: селектор контейнера.
            :param text: Текст, по которому ищется элемент.
            :param flag: Флаг точного совпадения текста.
            :return: Локатор найденного элемента.
            :raises AssertionError: если элемент не найден или не виден, или произошла ошибка.
        """
        try:
            locator = self.find(selector)
            target = locator.get_by_text(text, exact=flag)
            expect(target).to_be_visible(timeout=self.timeout)
            return target
        except TimeoutError:
            raise AssertionError(f'Элемент с текстом {text} не найден {selector}')
        except Error as e:
            raise AssertionError(f'Ошибка при получении элемента {selector} с текстом {text} {str(e)} ')


    def click_coordinates(self,selector: str, percent:float):
        """
            Производит клик по координатам внутри элемента, рассчитанным по проценту от ширины.

            :param selector: селектор элемента.
            :param percent: Процент по ширине элемента, где нужно кликнуть.
            :raises AssertionError: если произошла ошибка при вычислении координат или клике.
        """
        try:
            track = self.find(selector)
            box = track.bounding_box()
            x = box["x"] + box["width"] * percent
            y = box["y"] + box["height"] / 2
            print(x,y)
            self.page.mouse.click(x,y)
        except TimeoutError:
            raise AssertionError(f'Таймаут при клике на элемент {selector} по координатам')
        except Error as e:
            raise AssertionError(f'Ошибка при клике на элемент {selector} по координатам {str(e)} ')


    def reload(self):
        """
            Перезагружает текущую страницу и ожидает загрузки.

            :raises AssertionError: если страница не перезагрузилась или не достигла состояния 'domcontentloaded'.
        """
        try:
            self.page.reload()
            self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        except TimeoutError:
            raise AssertionError(f'Страница не перезагрузилась или не достигла состояния domcontentloaded')
        except Error as e:
            raise AssertionError(f'Ошибка при перезагрузке страницы {str(e)} ')


    def click_by_selector_and_text_and_index(self,selector: str,text: str, index: int):
        """
            Находит элемент по селектору и тексту, выбирает его по индексу и кликает.

            :param selector: селектор контейнера.
            :param text: Текст для поиска.
            :param index: Индекс элемента среди найденных с совпадением текста.
            :raises AssertionError: если элемент не найден или не кликабелен, или произошла ошибка.
        """
        try:
            locator = self.find(selector)
            target = locator.get_by_text(text,exact=True).nth(index)
            expect(target.to_be_visible, timeout = 5000)
            target.click()
        except TimeoutError:
            raise AssertionError(f'Не найден или не кликабелен элемент {selector} с текстом {text} и индексом {index}')
        except Error as e:
            raise AssertionError(f'Ошибка при клике на элемент {selector} с текстом {text} и индексом {index} {str(e)}')