import urllib
from io import BytesIO

from config import headers2

import pandas
from pandas import DataFrame


async def parser_xls(link: str, date: str, session) -> list[tuple]:
    """Парсит страницу, доставая из нее необходимые данные"""

    total_data_from_page = []
    df = await __filter_excel_by_pandas(link, session)

    for row in df.itertuples(index=True, name='Pandas'):
        try:
            exchange_product_id = row[1]
            exchange_product_name = row[2]
            delivery_basis_name = row[3]
            volume = int(row[4])
            total = int(row[5])
            count = int(row[6])
            total_data_from_page.append(
                (
                    exchange_product_id,
                    exchange_product_name,
                    exchange_product_id[:4],
                    exchange_product_id[4:7],
                    delivery_basis_name,
                    exchange_product_id[-1],
                    volume,
                    total,
                    count,
                    date,
                )
            )

        except Exception as e:
            print(f"Данные неверно спарсились, ошибка при попытке обращения к данным. Ошибка {e}")

    return total_data_from_page


async def __filter_excel_by_pandas(link: str, session) -> DataFrame:
    try:
        async with session.get(link, headers=headers2) as response:
            if response.status == 200:
                data = await response.read()
                link = BytesIO(data)
            else:
                print(f'Нет ответа от ссылки {link}')

    except Exception as e:
        print(e)
    except urllib.error.URLError as e:
        print(e.reason)

    """Чистка экселя, фильтрация данных"""
    df = pandas.read_excel(link, usecols='B:F,O')
    find_row_index = df[df.iloc[:, 0] == 'Единица измерения: Метрическая тонна'].index[0]
    start_row_index = find_row_index + 3
    end_row_index = df.iloc[start_row_index:, 0][
        (df.iloc[start_row_index:, 0] == 'Итого:') | (df.iloc[start_row_index:, 0].isna())].index[0]
    df = df.iloc[start_row_index:end_row_index]
    df.reset_index(drop=True, inplace=True)
    column_contract_count = df.columns[-1]
    df[column_contract_count] = pandas.to_numeric(df[column_contract_count], errors='coerce')
    df = df.dropna(subset=[column_contract_count])
    df = df[df[column_contract_count] > 0]

    return df
