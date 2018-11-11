import os
import click
import datetime

from dotenv import load_dotenv, find_dotenv

from chartmiru import create_app, app
from chartmiru.stock import Stock

@app.cli.command('register_stock', help='昨日の株取得')
def register_stock():
    pass

@app.cli.command('register_initial_stock', help='各銘柄の過去の株を取得する(手動)')
@click.argument('stock_code')
@click.argument('target_date', default=datetime.date.today())
@click.argument('from_date', required=False)
def register_initial_stock(stock_code: int, target_date, from_date):
    print(stock_code)
    print(target_date)
    print(from_date)
    stock = Stock()
    stock.get_row_stock(stock_code)

#TODO:撮り損ねた株を一気に回収するバッチ

if __name__ == 'cli':
    load_dotenv(find_dotenv())
    env_name = os.getenv('FLASK_CONFIG', 'default')
    create_app(env_name)
