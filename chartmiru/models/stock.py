from chartmiru.database import db
import datetime
from typing import List, Dict

from flask_sqlalchemy_session import current_session
from chartmiru import app, Database

class Stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    market = db.Column(db.String(50))
    open = db.Column(db.Integer)
    close = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    high = db.Column(db.Integer)
    low = db.Column(db.Integer)
    data_date = db.Column(db.DateTime)

    def __init__(self, company_id, open, close, volume, high, low, data_date):
        self.company_id = company_id
        self.open = open
        self.close = close
        self.volume = volume
        self.high = high
        self.low = low
        self.data_date = data_date

    # TODO:単数insert実装する
    @staticmethod
    def insert_stock(company_id: int, open: int, close: int, volume: int, high: int, low: int, data_date: datetime) -> int:
        stock = Stock(company_id, open, close, volume, high, low, data_date)
        current_session.add(stock)
        Database.flush()
        return stock.id

    @staticmethod
    def bulk_insert_stocks(stocks: List[Dict]) -> None:
        current_session.bulk_save_objects(
            [Stock(
                company_id=stock['company_id'],
                data_date=stock['data_date'],
                open=stock['open'],
                high=stock['high'],
                low=stock['low'],
                close=stock['close'],
                volume=stock['volume'])
                for stock in stocks], return_defaults=False)
        Database.commit()

