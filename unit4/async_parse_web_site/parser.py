import asyncio
import aiohttp
from bs4 import BeautifulSoup
from config import headers


async def collect_links() -> list[tuple[str, str]]:
    lst_data = await __gather_data()
    total_lst = []
    for lst in lst_data:
        total_lst.extend(lst)
    return total_lst


async def __gather_data() -> tuple[any]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 40, 1):
            task = asyncio.create_task(__collect_links_from_page(page=i, session=session))
            tasks.append(task)

        return await asyncio.gather(*tasks)


async def __collect_links_from_page(page, session) -> list[tuple[str, str]]:
    """Формируем результирующий лист для страницы-(линк : дата)"""
    result = []
    link, date = await __get_page_data(page, session)

    for x in range(len(link)):
        result.append((link[x], date[x]))

    return result


async def __get_page_data(page, session) -> tuple[list[str], list[str]]:
    """Сбор данных со страницы"""
    lst_href = []
    lst_dates = []

    url = f'https://spimex.com/markets/oil_products/trades/results/?page=page-{page}'

    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            await __collect_href(engine=soup, lst=lst_href)
            await __collect_dates(engine=soup, lst=lst_dates)

        else:
            print(f'Нет ответа от ссылки {url}')

    print(f'Обработал страницу {page}')

    return lst_href, lst_dates


async def __collect_href(engine: BeautifulSoup, lst: list) -> None:
    """# Находим ссылки на xls файлы в классе 'accordeon-inner__item-title link xls', выбираем только по
    string='text'"""
    for link in engine.findAll('a', class_='accordeon-inner__item-title link xls',
                               string='Бюллетень по итогам торгов в Секции «Нефтепродукты»'):
        href = link.get('href')
        if await __validate_href(href):
            lst.append(f'https://spimex.com{link.get('href')}')
        else:
            break


async def __collect_dates(engine: BeautifulSoup, lst: list) -> None:
    """"Собираем даты файлов"""
    for title in engine.findAll('div', class_='accordeon-inner__item-inner__title')[:10]:
        span = title.find('span')
        date = span.get_text(strip=True)
        if await __validate_date(date):
            lst.append(date)
        else:
            break


async def __validate_date(date: str) -> bool:
    year = date.split('.')
    year = int(year[-1])
    if year == 2024 or year == 2023:
        return True
    else:
        return False


async def __validate_href(href: str) -> bool:
    text_to_remove = '/upload/reports/oil_xls/oil_xls_'
    s = href.replace(text_to_remove, '')
    year = int(s[:4])
    if year == 2024 or year == 2023:
        return True
    else:
        return False
