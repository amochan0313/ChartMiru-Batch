import requests
import pandas as pd
import io
from typing import List, Dict

from flask_sqlalchemy_session import current_session

from chartmiru import app, Database
from chartmiru.models.stock import Stock

class Stocks:
    @classmethod
    def get_row_stocks(cls, stock_code: int, year: int) -> List[Dict]:
        # ユーザエージェントを指定しないと403返ってくる
        headers = {"User-agent":app.config['REQUEST_UA']}
        url = app.config['REQUEST_URI']
        try:
            payload = {'code': stock_code, 'year': year}
            stock_data = requests.post(url, data=payload, headers=headers)
            df = pd.read_csv(io.StringIO(stock_data.content.decode('shift-jis')), header=1)
            formatted_data = []
            for index, row in df.iterrows():
                formatted_data.append(
                    {
                        'company_id': stock_code,
                        'data_date': row['日付'],
                        'open': row['始値'],
                        'high': row['高値'],
                        'low': row['安値'],
                        'close': row['終値'],
                        'volume': row['出来高'],
                    }
                )
            return formatted_data

        except requests.exceptions.RequestException as err:
            print(err)
