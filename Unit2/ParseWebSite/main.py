from Unit2.ParseWebSite.core import init_db_parce, insert_data
from Unit2.ParseWebSite.pandasParser import parser_xls
from Unit2.ParseWebSite.parser import collect_links

if __name__ == '__main__':
    init_db_parce()
    links = collect_links()
    for link in links:
        data_from_page = parser_xls(link)
        insert_data(data_from_page)
