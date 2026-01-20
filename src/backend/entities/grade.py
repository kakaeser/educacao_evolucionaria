from sqlalchemy import Column, String, Integer, ForeignKey
from config.base import Base
from sqlalchemy.orm import relationship

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    term_id = Column(Integer, ForeignKey("terms.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")