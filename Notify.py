"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    notify create_note <note_content>
    notify view_note <note_id>
    notify delete_note <note_id>
    notify view_all_notes
    notify search_note <note_content>
    notify export_json
    notify import_json
    notify sync
    notify (-i | --interactive)
    notify (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import Figlet
from database import create_db, Base, Notes
from note_taking_logic import Note
from termcolor import colored
from tabulate import tabulate
from colorama import init, Fore, Back,Style
init()

notify = Note()



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

    prompt = ("notify: ")


    file = None

    @docopt_cmd
    def do_create_note(self, arg):
        """Usage: create_note <note_content>..."""
        
        new_note = arg["<note_content>"]
        notify.create_note(new_note)

    @docopt_cmd
    def do_view_note(self, arg):
        """Usage: view_note <note_id>"""
        view_1 = arg["<note_id>"]
        notify.view_note(view_1)

    @docopt_cmd
    def do_delete_note(self, arg):
        """Usage: view_note <note_id>"""
        delete_1 = arg["<note_id>"]
        notify.delete_note(delete_1)

    @docopt_cmd
    def do_view_all_notes(self, args):
        """Usage: view_all_notes"""
        notify.view_all_notes()

    @docopt_cmd
    def do_search_note(self, arg):
        """Usage: search_note <note_content>"""
        search_it = arg["<note_content>"]
        notify.search_note(search_it)

    @docopt_cmd
    def do_export_json(self, args):
        """Usage: export_json"""
        notify.export_json()

    @docopt_cmd
    def do_import_json(self, args):
        """Usage: view_note"""
        notify.import_json()

    @docopt_cmd
    def do_sync(self, args):
        """Usage: sync"""
        notify.sync()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:], help = True)
print (__doc__)

if opt['--interactive']:
    Notify().cmdloop()

print(opt)