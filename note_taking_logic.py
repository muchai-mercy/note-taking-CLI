from sqlalchemy.orm import Session
from database import Notes, create_db, Base

class Note():

	def __init__ (self, note_content, note_id):
		self.note_content = note_content
		self.note_id = note_id
	
	def create_note(note_content):
		new_note = Notes(note_content = note_content)
		engine = create_db()
		Base.metadata.bind = engine
		session = Session()
		session.add(new_note)
		session.commit()
	
	def view_note(note_id):
		session = Session()
		result = session.query(Notes).filter_by(note_id = note_id).first()
		print ("Id: " + str(result.note_id) + " Content: " + result.note_content)

	def view_all_notes():
		session = Session()
		result = session.query(Notes).all()
		print(result)
		for item in result:
			print ("Id: " + str(item.note_id) + " Content: " + item.note_content)

	def delete_note(note_id):
		session = Session()
		note_to_delete = session.query(Notes).filter_by(note_id = note_id).first()
		deleted = session.delete(note_to_delete)
		print("Id " + str(note_to_delete.note_id) + " deleted!")

	def search_note(note_content):
		session = Session()
		results = session.query(Notes).filter_by(note_content = note_content).all()
		note_list = []

		for result in results:
			search_query = note_list.append(result.note_content)
			for item in note_list:
				print (note_list)
		# if note_content['<text>'] in item:
				# 	print ('Okay')

Note.create_note('lfuhkf;jpi;')

Note.view_note(1)
# Note.view_note(1)
# print(note.note_content)
Note.view_all_notes()

Note.delete_note(2)

Note.search_note("lfuhkf;jpi;")