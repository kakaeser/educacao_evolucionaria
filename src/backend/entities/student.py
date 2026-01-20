from sqlalchemy import Column, String, Integer, ForeignKey
from backend.config.base import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ra = Column(String)
    classroom = Column(String)

    user = relationship("User", back_populates="student")
    grades = relationship("Grade", back_populates="student")

    
