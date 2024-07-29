import requests
from bs4 import BeautifulSoup

from config import HEADER


def collect_links() -> list[tuple[str, str]]:
    """Формируем результирующий лист -(линк : дата)"""
    result = []
    link, date = __collect_links_date_from_pages()

    for x in range(len(link)):
        result.append((link[x], date[x]))

    return result


def __collect_links_date_from_pages() -> tuple[list[str], list[str]]:
    """Собираем ссылки и даты со всех страниц"""
    lst_links = []
    lst_dates = []

    for i in range(1, 2, 1):
        url = f'https://spimex.com/markets/oil_products/trades/results/?page=page-{i}'
        headers = {"User-Agent": HEADER}

        req = requests.get(url=url, headers=headers)
        html = req.text

        soup = BeautifulSoup(html, 'lxml')

        __collect_href(engine=soup, lst=lst_links)
        __collect_dates(engine=soup, lst=lst_dates)

    return lst_links, lst_dates


def __collect_href(engine: BeautifulSoup, lst: list) -> None:
    """# Находим ссылки на xls файлы в классе 'accordeon-inner__item-title link xls', выбираем только по
    string='text'"""
    for link in engine.findAll('a', class_='accordeon-inner__item-title link xls',
                               string='Бюллетень по итогам торгов в Секции «Нефтепродукты»'):
        href = link.get('href')
        if __validate_href(href):
            lst.append(f'https://spimex.com{link.get('href')}')
        else:
            break


def __collect_dates(engine: BeautifulSoup, lst: list) -> None:
    for title in engine.findAll('div', class_='accordeon-inner__item-inner__title')[:10]:
        span = title.find('span')
        date = span.get_text(strip=True)
        if __validate_date(date):
            lst.append(date)
        else:
            break


def __validate_href(href: str) -> bool:
    text_to_remove = '/upload/reports/oil_xls/oil_xls_'
    s = href.replace(text_to_remove, '')
    year = int(s[:4])
    if year == 2024 or year == 2023:
        return True
    else:
        return False


def __validate_date(date: str) -> bool:
    year = date.split('.')
    year = int(year[-1])
    if year == 2024 or year == 2023:
        return True
    else:
        return False


# print(*__collect_links_date_from_pages(), sep='\n')


