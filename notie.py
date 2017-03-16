"""
Usage:
    my_app (-i | --interactive)
    my_app (-h | --help | --version)
    create_note <note_content>
    view_note <note_id>
    delete_note <note_id>
    view_all_notes <>
    search_note <note_content>
    export_json <>
    import_json <>
    sync <>

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

class Notify(cmd.Cmd):
    print(colored("*-*" * 80, "cyan"))
    print(colored(Figlet(font='slant').renderText('\t NOTIFY'),"magenta"))
    print(colored("*-*" * 80, "cyan"))
    print(colored("\t Welcome to Notify! ","yellow"))
    print(colored("\t You can write notes here and store them...","green"))
    
    prompt = ("Get started with Notify")
    file = None

    @docopt_cmd
    def do_create_note(self, arg):
        """Usage: create_note <note_content>"""
        note_content =arg["<note_content>"]
        create_note(note_content)
        print(note_content)

    @docopt_cmd
    def do_view_note(self, arg):
        """Usage: view_note <note_id>"""
        note_id = arg["<note_id>"]
        view_note(note_id)

    @docopt_cmd
    def do_view_all_notes(self, arg):
        """Usage: view_all_notes <note_id>"""
        note_id = arg["<note_id>"]
        view_all_notes(note_id)

    @docopt_cmd
    def do_delete_note(self, arg):
        """Usage: delete_note <note_id>"""
        note_id = arg["<note_id>"]
        delete_note(note_id)

    @docopt_cmd
    def do_search_note(self, arg):
        """Usage: search_note <note_content>"""
        note_content = arg["<note_content>"]
        search_note(note_content)

    @docopt_cmd
    def do_view_note(self, arg):
        """Usage: view_note <note_id>"""
        note_id = arg["<note_id>"]
        view_note(note_id)

    @docopt_cmd
    def do_export_json(self):
        """Usage: export_json <>"""
        export_json()

    @docopt_cmd
    def do_import_json(self):
        """Usage: view_note <>"""
        import_json()

    # @docopt_cmd
    # def do_sync(self):
    #     """Usage: sync <>"""
    #     sync()

    @docopt_cmd    
    def do_quit(self, arg):
        """Usage: quit"""

        print("Your notes are saved!Goodbye")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        Notify().cmdloop()
    except Exception as exc:
        print('Exiting Notify')