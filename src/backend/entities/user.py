from sqlalchemy import Column, String, Integer
from config.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String, unique = True)
    passwor_hash = Column(String)
    role = Column(String)

    student = relationship("Student", back_populates="user")