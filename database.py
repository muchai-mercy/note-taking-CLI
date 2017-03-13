from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///note_taking.db')


class Notes(Base):

    __tablename__ = 'notes'
    #Table of the notes, containing IDs, content and status

    id = Column(Integer, primary_key=True)
    note_content = Column(String(20), nullable=False)
   

Base.metadata.create_all(engine)