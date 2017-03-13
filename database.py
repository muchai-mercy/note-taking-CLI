from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
class Notes():

    __tablename__ = 'notes'
    #Table of the notes, containing IDs, content and status

    id = Column(Integer, primary_key=True)
    note_content = Column(String(20), nullable=False)
    
    def __init__ (self):
    	self.create = str('')






