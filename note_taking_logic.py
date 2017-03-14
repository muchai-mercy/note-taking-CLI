from sqlalchemy.orm import Session
from database import Notes, create_db, Base

class Note():
	
	def create_note(self, note_content):
		self.note_content = note_content
		note = Notes(note_content = self.note_content)
		engine = create_db()
		Base.metadata.bind = engine
		session = Session()
		session.add(note)
		session.commit()
	
	def view_note(self, id):
		self.id = id
		id = Notes(id = self.id)

notes = Note()
notes.create_note("today is Tuesday")

