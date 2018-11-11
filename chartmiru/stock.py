import requests

from chartmiru import app

class Stock:
    @classmethod
    def get_row_stock(cls, stock_code):
        # ユーザエージェントを指定しないと403返ってくる
        headers = {"User-agent":app.config['REQUEST_UA']}
        url = app.config['REQUEST_URI']
        try:
            payload = {'code': stock_code, 'year': '2018'}
            r = requests.post(url, data=payload, headers=headers)
            print(r.text)
        except requests.exceptions.RequestException as err:
            print(err)
