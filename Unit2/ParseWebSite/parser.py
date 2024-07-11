import requests
from bs4 import BeautifulSoup
from Unit2.ParseWebSite.config import HEADER


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


def __collect_links_date_from_pages() -> tuple[list[str], list[str]]:
    """Собираем ссылки и даты со всех страниц"""
    lst_links = []
    lst_dates = []

    for i in range(1, 40, 1):
        url = f'https://spimex.com/markets/oil_products/trades/results/?page=page-{i}'
        req = requests.get(url=url, headers={"User-Agent": HEADER})
        html = req.text
        # Находим ссылки на xls файлы в классе 'accordeon-inner__item-title link xls', выбираем только по string='text'
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.findAll('a', class_='accordeon-inner__item-title link xls',
                                 string='Бюллетень по итогам торгов в Секции «Нефтепродукты»'):
            href = link.get('href')
            if __validate_href(href):
                lst_links.append(f'https://spimex.com{link.get('href')}')
            else:
                break

        for title in soup.findAll('div', class_='accordeon-inner__item-inner__title')[:10]:
            span = title.find('span')
            date = span.get_text(strip=True)
            if __validate_date(date):
                lst_dates.append(date)
            else:
                break

    return lst_links, lst_dates


def collect_links() -> list[tuple[str, str]]:
    """Формируем результирующий лист -(линк : дата)"""
    result = []
    link, date = __collect_links_date_from_pages()

    for x in range(len(link)):
        result.append((link[x], date[x]))

    return result


