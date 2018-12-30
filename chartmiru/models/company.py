from chartmiru.database import db
import datetime
from typing import List, Dict

from flask_sqlalchemy_session import current_session
from chartmiru import app, Database

class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    initialized = db.Column(db.Integer)

    def __init__(self, id, name, initialized):
        self.id = id
        self.name = name
        self.initialized = initialized

    @staticmethod
    def get_companies(initialized: bool = None) -> List:
        query = current_session.query(Company)
        query = query.filter_by(initialized=initialized) if initialized is not None else query
        companies = query.all()
        Database.flush()
        if companies is None:
            return []
        return list(map(lambda company: {
            'id': company.id,
            'name': company.name
        }, companies))


    @staticmethod
    def update_company(id: int, initialized: bool = None) -> None:
        company = current_session.query(Company).get(id)
        company.initialized = initialized if initialized else company.initialized
        current_session.add(company)
        Database.commit()
