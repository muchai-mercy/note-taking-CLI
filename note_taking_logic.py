from sqlalchemy.orm import Session
from database import Notes, create_db, Base
import json
from firebase import firebase

engine = create_db()
Base.metadata.bind = engine
session = Session()


class Note():

	# def __init__ (self):
	# 	self.note_content = note_content
	# 	self.note_id = note_id
	# 	self.page_size = int(page_size)
	# 	self.page = int(page)
		
	
	
	def create_note(self, note_content):
		self.note_content = note_content
		"""Create a new note and store it in database"""
		new_note = Notes(note_content = note_content)
		session.add(new_note)
		session.commit()
		print ("New note created!: " + str(note_content))

	"""View any note created using the Id"""
	def view_note(self, note_id):
		result = session.query(Notes).filter_by(note_id = note_id).first()
		print ("Id: " + str(result.note_id) + " Content: " + result.note_content)

	""" View a formated list of all notes"""
	def view_all_notes(self):
		result = session.query(Notes).all()
		# print(result)
		for item in result:
			print ("Id: " + str(item.note_id) + " Content: " + item.note_content)

	"""Delete a note. Filter note to delete using note ID"""

	def delete_note(self, note_id):
		note_to_delete = session.query(Notes).filter_by(note_id=note_id).first()
		deleted = session.delete(note_to_delete)
		print("Id " + str(note_to_delete.note_id) + " deleted!")

	"""Search for all notes that include a queried text
		Filter all notes with text
		Return a list of all notes that have text"""

	def search_note(self, note_content, page = 0, page_size = 20):
		results = session.query(Notes).filter(Notes.note_content.ilike("%" + note_content + "%"))
		if page_size:
			results = results.limit(page_size)
		if page:
			results = results.offset(page*page_size)
		note_list = {}
		for result in results:
			note_list[result.note_id] = result.note_content
		print(note_list)


	"""Imports notes as JSON file"""
	def import_json(self):
		with open("Notify.txt") as (json_file):
			notes_file = json.load(json_file)
			print("You have imported a JSON file called Notify")
			print(notes_file)

	"""Exports notes as JSON file"""
	def export_json(self):
		my_file	= []
		for table in session.query(Notes).all():
			my_js = dict(table.__dict__)
			my_js.pop('_sa_instance_state', None)
			my_file.append(my_js)

		with open('Notify.txt', 'w') as json_file:
			json.dump(my_file, json_file, indent = 4)
			print("File exported successfuly!")

	"""Synchronises Notes with online datastore Firebase"""
	def sync(self):
		notify_app = firebase.FirebaseApplication('https://notify-74072.firebaseio.com/', None)
		my_file	= []
		for table in session.query(Notes).all():
			my_js =  dict(table.__dict__)
			my_js.pop('_sa_instance_state', None)
			my_file.append(my_js)
		notes_table = notify_app.post('/notes', my_file)
		print ("Notify file has been synced")
			

# bar = Note()
# bar.create_note("I like mangoes")
# # Note.view_note(1)

# # Note.view_all_notes()

# # Note.delete_note(2)
# # Note.search_note("ay")
# # Note.import_json()
# # Note.export_json()
# # Note.sync()