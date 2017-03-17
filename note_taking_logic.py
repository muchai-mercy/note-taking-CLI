from sqlalchemy.orm import Session
from database import Notes, create_db, Base
import json
from firebase import firebase

engine = create_db()
Base.metadata.bind = engine
session = Session()


class Note():
		
	def create_note(self, note_content):
		"""Create a new note and store it in database"""
		# cont = input("enter new note: ")
		new_note = Notes(note_content = note_content)
		session.add(new_note)
		session.commit()
		print ("New note created!: " + str(note_content))

	def view_note(self, note_id):
		"""View any note created using the Id"""
		if type(note_id) == int and note_id != 0:
			result = session.query(Notes).filter_by(note_id = note_id).first()
			print("Here is the note you want to view:")
			print ("Id: " + str(result.note_id) + " Content: " + result.note_content)
			
		else:
			print ("Oops! Invalid note_id")

			
	
	def view_all_notes(self):

		""" View a formated list of all notes"""

		result = session.query(Notes).all()
		print("All notes are here:")
		for item in result:
			print ("Id: " + str(item.note_id) + " Content: " + item.note_content)

	
	def delete_note(self, note_id):

		"""Delete a note. Filter note to delete using note ID"""

		note_to_delete = session.query(Notes).filter_by(note_id=note_id).first()
		deleted = session.delete(note_to_delete)
		session.commit()
		print("You just deleted " + "Id " + str(note_to_delete.note_id) + "!")


	def search_note(self, note_content, page = 0, page_size = 20):

		"""Search for all notes that include a queried text
		Filter all notes with text
		Return a list of all notes that have text"""
		results = session.query(Notes).filter(Notes.note_content.ilike("%" + note_content + "%"))
		if page_size:
			results = results.limit(page_size)
		if page:
			results = results.offset(page*page_size)
		note_list = {}
		for result in results:
			note_list[result.note_id] = result.note_content
		print ("Find a dictionary of all the notes with the text you just searched here:")
		print(note_list)

	def import_(self):

		"""Imports file of notes"""

		with open("Notify.txt") as json_file:
			notes_file = json.load(json_file)
			print("You have imported a file called Notify. Here it is!")
			print(notes_file)

	def export_(self):

		"""Exports notes as a file"""

		my_file	= []
		for table in session.query(Notes).all():
			my_js = dict(table.__dict__)
			my_js.pop('_sa_instance_state', None)
			my_file.append(my_js)

		with open('Notify.txt', 'w') as json_file:
			json.dump(my_file, json_file, indent = 4)
			print("File exported successfuly!")
			print("You can now find the Notify.txt file locally.")

	def sync(self):

		"""Synchronises Notes with online datastore Firebase"""

		notify_app = firebase.FirebaseApplication('https://notify-74072.firebaseio.com/', None)
		my_file	= []
		for table in session.query(Notes).all():
			my_js =  dict(table.__dict__)
			my_js.pop('_sa_instance_state', None)
			my_file.append(my_js)
		notes_table = notify_app.post('/notes', my_file)
		print("Syncing your notes to Firebase")
		print ("Yaay! All notes have been synced!")

