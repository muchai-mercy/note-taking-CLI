from sqlalchemy.orm import Session
from database import Notes, create_db, Base

class Note():
	
	def create_note(self, note_content):
		self.note_content = note_content
		new_note = Notes(note_content = self.note_content)
		engine = create_db()
		Base.metadata.bind = engine
		session = Session()
		session.add(new_note)
		session.commit()
	
	def view_note(self, note_id):
		self.note_id = note_id
		session = Session()
		result = session.query(Notes).filter_by(note_id = self.note_id).first()
		print ("Id: " + str(result.note_id) + " Content: " + result.note_content)

	def view_all_notes(self):
		session = Session()
		result = session.query(Notes).all()
		print(result)
		for item in result:
			print ("Id: " + str(item.note_id) + " Content: " + item.note_content)

	def delete_note(self, note_id):
		self.note_id = note_id
		session = Session()
		note_to_delete = session.query(Notes).filter_by(note_id = self.note_id).first()
		deleted = session.delete(note_to_delete)
		print("Id " + str(note_to_delete.note_id) + " deleted!")

	def search_note(self,note_content):
		self.note_content = str(note_content)
		session = Session()
		results = session.query(Notes).filter_by(note_content = self.note_content).all()
		note_list = []

		for result in results:
			search_query = note_list.append(result.note_content)
			for item in note_list:
				# if note_content['<text>'] in item:
				# 	print ('Okay')
					print (note_list)


notes = Note()
notes.create_note('lfuhkf;jpi;')

first_1 = Note()
first_1.view_note(1)
# Note.view_note(1)
# print(note.note_content)
all_notes = Note()
all_notes.view_all_notes()

delete_1 = Note()
delete_1.delete_note(2)

searching = Note()
searching.search_note("lfuhkf;jpi;")