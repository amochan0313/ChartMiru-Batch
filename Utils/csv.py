import requests
import io
import pandas as pd
from typing import List, Dict

class Csv():
    @staticmethod
    def convert_csv_list(stock_data: object, stock_code: int) -> List[Dict]:
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
