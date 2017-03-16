"""
Usage:
    my_app (-i | --interactive)
    my_app (-h | --help | --version)
    create_note <note_content>
    view_note <note_id>
    delete_note <note_id>
    view_all_notes <>
    search_note <note_content>

Options:
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from colorama import init, Fore
init()
from pyfiglet import Figlet
from database import create_db, Base, Notes
from note_taking_logic import Note
from termcolor import colored
from tabulate import tabulate
from colorama import init, Fore, Back, Style
init()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
            

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class Note(cmd.Cmd):
    print("*-*" * 80)
    print(colored(Figlet(font='slant').renderText('\t NOTIFY'),"magenta"))
    print("*-*" * 80)
    print(colored("\t Take Notes Here: ","yellow"))
    print(" \tThis application helps you write notes and store them", "white")
    
    prompt = '(class_attendance) '
    file = None

    @docopt_cmd
    def do_create_note(self, arg):# This command creates a new student in the database and generate an id for the student
        """Usage: add_student <regno>    """
        note_content =arg["<note_content>"]
        create_note(note_content)        

        print(note_content)

    # def do_student_remove(self, arg):
    #     """Usage: student_remove <studentid>"""
    #     # print (arg)
    #     student_id = arg
    #     remove_student(student_id)
    #     print(student_id)

    # @docopt_cmd
    # def do_add_class(self, arg):
    #     """Usage: add_class <classcode>"""
    #     class_code = arg ["<classcode>"]
    #     add_new_class(class_code)

    #     print(class_code)

    # @docopt_cmd   
    # def do_class_remove(self,arg):
    #     """Usage: class_remove <classid> """
    #     class_id = arg ["classid"]
    #     remove_class(class_id)

    #     print(class_id)

    # @docopt_cmd    
    # def do_student_list(self,arg):
    #     """Usage: student_list """
    #     all_students()
        

    # @docopt_cmd
    # def do_class_list(self,arg):
    #     """Usage: class_list"""
    #     all_classes()

    # @docopt_cmd
    # def do_checkin(self, arg):
    #     """Usage: checkin <studentid> <classid>"""
    #     try:
    #         student_id = arg["<studentid>"]
    #         class_id = arg["<classid>"]
    #         check_in_student(int(student_id), int(class_id))
    #     except Exception as exc:
    #         print('Error Occurred')
    #         print(student_id + " has been checked into class " + class_id )

    # @docopt_cmd
    # def do_checkout(self,arg):
    #     """Usage: checkout <studentid> <classid>"""
    #     try:
    #         student_id = int(arg["<studentid>"])
    #         class_id = int(arg["<classid>"])
    #         check_out_student(student_id, classid)
            
    #     except Exception:
    #         print('Invalid Values. Use numbers')
    #         return
        

    # @docopt_cmd
    # def do_signup(self,arg):
    #     """Usage: signup <user_name> <pass_word>"""
    #     username = arg["user_name"]
    #     password = arg["pass_word"]
    #     print(username, password)

    @docopt_cmd    
    def do_quit(self, arg):
        """Usage: quit"""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        MyInteractive().cmdloop()
    except Exception as exc:
        print('Exiting')