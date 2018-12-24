from chartmiru.database import db
import datetime
from typing import List, Dict

from flask_sqlalchemy_session import current_session
from chartmiru import app, Database

class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_companies() -> List:
        query = current_session.query(Company)
        companies = query.all()
        Database.flush()
        if companies is None:
            return []
        return list(map(lambda company: {
            'id': company.id,
            'name': company.name
        }, companies))