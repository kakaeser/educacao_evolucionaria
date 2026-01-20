from sqlalchemy import Column, String, Integer
from config.base import Base
from sqlalchemy.orm import relationship

class SchoolClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    class_name = Column(String)
