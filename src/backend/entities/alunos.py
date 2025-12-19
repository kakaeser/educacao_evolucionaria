from sqlalchemy import Column, String, Integer
from backend.config.base import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable= False)
    ra = Column(String, nullable= False, unique=True)
    senha = Column(String, nullable= False)
    bday = Column(String, nullable= False)
    turma = Column(String, nullable= False)
    faltas = Column(Integer)
