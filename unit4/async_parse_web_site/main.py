import time

from unit4.async_parse_web_site.core import init_db_parce, insert_data
from unit4.async_parse_web_site.pandas_parser import parser_xls
from unit4.async_parse_web_site.parser import collect_links


# from unit2.async_parse_web_site.core import init_db_parce, insert_data
# from unit2.async_parse_web_site.pandas_parser import parser_xls
# from unit2.async_parse_web_site.parser import collect_links


def main() -> None:
    init_db_parce()
    links = collect_links()

    for link, date in links:
        data_from_page = parser_xls(link, date)
        insert_data(data_from_page)


if __name__ == '__main__':
    start = time.time()
    start2 = time.monotonic()
    main()
    finish = time.time()
    finish2 = time.monotonic()
    res = finish - start
    res2 = finish2 - start2

    print('Время работы в секундах: ', res)
    print('Время работы в секундах: ', res2)

#  Время работы в секундах:  484.11316776275635
# Время работы в секундах:  484.10208203100046
#Ч:М:С -> 0:08:04.113168
#Ч:М:С -> 0:08:04.102082

#
# Время работы в секундах:  470.4362630844116
# Время работы в секундах:  470.42214723399957