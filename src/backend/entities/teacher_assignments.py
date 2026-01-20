from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from config.base import Base
from sqlalchemy.orm import relationship

class TeacherAssignments(Base):
    __tablename__ = "teacher_assignments"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"),nullable = False)
    subject_id = Column(Integer, ForeignKey("subjects.id"),nullable = False)
    class_id = Column(Integer, ForeignKey("classes.id"),nullable = False)

    ano_letivo = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)
    
    school_class = relationship("SchoolClass")
    subject = relationship("Subject")
    teacher = relationship("Teacher", back_populates = "assignments")