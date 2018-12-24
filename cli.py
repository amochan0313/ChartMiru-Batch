import os
import click
import datetime

from dotenv import load_dotenv, find_dotenv

from chartmiru import create_app, app
from chartmiru.stocks import Stocks
from chartmiru.models.stock import Stock

@app.cli.command('register_stock', help='昨日の株取得')
def register_stock():
    pass

@app.cli.command('register_initial_stock', help='各銘柄の過去の株を取得する')
@click.argument('stock_code')
@click.argument('target_year', default=datetime.date.today().year)
@click.argument('from_year', default=datetime.date.today().year)
def register_initial_stock(stock_code: int, target_year: int, from_year: int):
    s = Stocks()
    for year in range(from_year, target_year + 1):
        stocks= s.get_row_stocks(stock_code, year)
        Stock.bulk_insert_stocks(stocks)



#TODO:撮り損ねた株を一気に回収するバッチ

if __name__ == 'cli':
    load_dotenv(find_dotenv())
    env_name = os.getenv('FLASK_CONFIG', 'default')
    create_app(env_name)
