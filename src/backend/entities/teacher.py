from sqlalchemy import Column, String, Integer, ForeignKey
from config.base import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
    assignments = relationship("TeacherAssignment", back_populates = "teacher", cascade = "all, delete-orphan")