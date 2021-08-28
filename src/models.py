from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime)
