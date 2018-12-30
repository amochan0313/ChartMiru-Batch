import requests
from typing import List, Dict

from flask_sqlalchemy_session import current_session

from chartmiru import app, Database
from chartmiru.models.stock import Stock
from Utils.csv import Csv

class Stocks:
    @classmethod
    def get_row_stocks(cls, stock_code: int, year: int) -> List[Dict]:
        # ユーザエージェントを指定しないと403返ってくる
        headers = {"User-agent":app.config['REQUEST_UA']}
        url = app.config['REQUEST_URI']
        try:
            payload = {'code': stock_code, 'year': year}
            stock_data = requests.post(url, data=payload, headers=headers)
            return Csv.convert_csv_list(stock_data, stock_code)

        except requests.exceptions.RequestException as err:
            print(err)
