from sqlalchemy import Column, String
from backend.config.base import Base
from sqlalchemy.orm import relationship

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    sub_name = Column(String)

    grades = relationship("Grade", back_populates="subject")