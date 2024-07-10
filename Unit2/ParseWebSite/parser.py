import requests
from bs4 import BeautifulSoup

from Unit2.ParseWebSite.config import HEADER

# ParseResult = collections.namedtuple(
#     'ParseResult',
#     (
#         'title',
#         'url'
#     )
#
# )

products = []
years = []
headers = {
    "User-Agent": HEADER
}


def __validate(href: str):
    text_to_remove = '/upload/reports/oil_xls/oil_xls_'
    s = href.replace(text_to_remove, '')
    year = int(s[:4])
    if year == 2024 or year == 2023:
        return True
    else:
        return False


def collect_links():
    for i in range(1):
        url = f'https://spimex.com/markets/oil_products/trades/results/?page=page-{i}'
        req = requests.get(url=url, headers=headers)
        html = req.text
        # Находим ссылки на xls файлы в классе 'accordeon-inner__item-title link xls', выбираем только по string='text'
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.findAll('a', class_='accordeon-inner__item-title link xls',
                                 string='Бюллетень по итогам торгов в Секции «Нефтепродукты»'):
            href = link.get('href')
            if __validate(href):
                products.append(f'https://spimex.com{link.get('href')}')

        for title in soup.findAll('div', class_='accordeon-inner__item-inner__title')[:10]:
            span = title.find('span')
            date = span.get_text()
            years.append(date)

    return products


print(collect_links())
