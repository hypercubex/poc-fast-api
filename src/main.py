from typing import List, Optional
import datetime

from sqlalchemy.engine.base import Transaction
from sqlalchemy.sql import func

from fastapi import FastAPI, Depends
# from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Session, engine
from models import Transaction
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/transactions", )
async def find_transactions(
    user_id: int,
    after: Optional[datetime.datetime] = None,
    before: Optional[datetime.datetime] = None,
    interval: Optional[int] = None,
    limit: Optional[int] = 10,
    start: Optional[int] = 0,
    db: Session = Depends(get_db)
):

    query = db.query(Transaction)\
        .where(Transaction.user_id == user_id)

    if after is not None:
        query = query.where(Transaction.created_at >= after)
    if before is not None:
        query = query.where(Transaction.created_at <= before)
    if interval is not None:
        after_hours = datetime.datetime.now() - datetime.timedelta(hours=interval)
        query = query.where(Transaction.created_at >= after_hours)

    return {
        'transactions': query.offset(start).limit(limit).all(),
        **query.with_entities(func.sum(Transaction.amount).label(
            "total_amount")).group_by(Transaction.user_id).all()[0]
    }
