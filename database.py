from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Notes(Base):

    __tablename__ = 'notes'
    #Table of the notes, containing IDs, content

    note_id = Column(Integer, primary_key = True)
    note_content = Column(String(600), nullable = False)

def create_db():
	engine = create_engine('sqlite:///note_taking.db') 	
	Base.metadata.create_all(engine)
	return engine
