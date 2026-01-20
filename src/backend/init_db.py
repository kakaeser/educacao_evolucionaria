from entities.grade import Grade
from entities.student import Student
from entities.subject import Subject
from entities.term import Term
from entities.user import User
from entities.school_class import SchoolClass
from entities.teacher import Teacher
from entities.teacher_assignments import TeacherAssignments

from config.connection import DBConnectionHandler
from config.base import Base

db_handler = DBConnectionHandler()
engine = db_handler.get_engine()

Base.metadata.create_all(bind=engine)