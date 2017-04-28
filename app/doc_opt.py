#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    app create_room <room_arguments>...
    app add_person <person_arguments>...
    app (-i | --interactive)
    app (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app import app


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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to The Office Space Allocation App!' \
        + ' (type help for a list of commands.)'
    prompt = '(The Office Space Allocator) '
    file = None

    @docopt_cmd
    def do_create_room(self, arguments):
        """Usage: create_room <room_arguments>... """
        room_arguments = arguments['<room_arguments>']
        print(app.create_room_buffer(room_arguments))
        print('New room count: ',len(app.the_dojo.rooms))

    @docopt_cmd
    def do_add_person(self, arguments):
        """Usage: add_person <person_arguments>... """
        person_arguments = arguments['<person_arguments>']
        print(app.add_person_buffer(person_arguments))
        print('Allocated: ', len(app.get_all_office_occupants()) + len(app.get_all_livingspace_occupants()))
        print('Unallocated: ', len(app.unallocated_people))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)