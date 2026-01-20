from sqlalchemy import Column, String, Integer
from backend.config.base import Base

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True)
    term_name = Column(String)
    ano = Column(Integer)