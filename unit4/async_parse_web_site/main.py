import asyncio
import time
import aiohttp

from unit4.async_parse_web_site.core import init_db_parce, insert_data
from unit4.async_parse_web_site.pandas_parser import parser_xls
from unit4.async_parse_web_site.parser import collect_links


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        await init_db_parce()
        links = await collect_links()

        tasks = []
        for link, date in links:
            data_from_page = await parser_xls(link, date, session)
            task2 = asyncio.create_task(insert_data(data_from_page))
            tasks.append(task2)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()

    asyncio.run(main())

    finish = time.time()
    res = finish - start

    print('Время работы в секундах: ', res)

