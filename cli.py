import os
import click
import datetime

from dotenv import load_dotenv, find_dotenv

from chartmiru import create_app, app
from chartmiru.stocks import Stocks
from chartmiru.models.stock import Stock
from chartmiru.models.company import Company

STOCK_DATA_INITIALIZED = True

@app.cli.command('register_stock', help='各銘柄の昨日の株取得')
def register_stock():
    companies = Company.get_company(STOCK_DATA_INITIALIZED)
    s = Stocks()
    for company in companies:
        stocks = s.get_row_stocks(company['id'], datetime.date.today().year)
        latest_data = stocks[-1]
        '''
        祝日にバッチが回った時はデータが被ってしまうので更新しない
        また何らかの理由により参照元データが更新されていない場合はDBとデータが被ってしまうので更新しない
        '''
        if s.exist_latest_data(company['id'], latest_data['data_date']):
            #TODO: log出力したい
            continue
        Stock.insert_stock(
            latest_data['company_id'],
            latest_data['open'],
            latest_data['close'],
            latest_data['volume'],
            latest_data['high'],
            latest_data['low'],
            latest_data['data_date']
        )



@app.cli.command('register_initial_stock', help='各銘柄の過去の株を取得する')
@click.argument('target_year', default=datetime.date.today().year)
@click.argument('from_year', default=datetime.date.today().year)
def register_initial_stock(target_year: int, from_year: int):
    companies = Company.get_company(not STOCK_DATA_INITIALIZED)
    s = Stocks()
    for company in companies:
        # 初期化する時は元のデータを一度すべて消す
        Stock.delete_stock(company['id'])
        for year in range(from_year, target_year + 1):
            stocks= s.get_row_stocks(company['id'], year)
            Stock.bulk_insert_stocks(stocks)
            Company.update_company(company['id'], STOCK_DATA_INITIALIZED)


#TODO:撮り損ねた株を一気に回収するバッチ

if __name__ == 'cli':
    load_dotenv(find_dotenv())
    env_name = os.getenv('FLASK_CONFIG', 'default')
    create_app(env_name)
