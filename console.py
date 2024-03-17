#!/usr/bin/python3

"""
Console Module
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    # Prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    # Dictionary mapping class names to their respective classes
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    # List of dot commands
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    # Dictionary of types for attribute values
    types = {
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'latitude': float,
        'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""
        # Reformatting the command line for advanced command syntax
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            # Parsing the command line
            parsed_line = line[:]

            class_name = parsed_line[:parsed_line.find('.')]
            command = parsed_line[parsed_line.find('.') + 1:parsed_line.find('(')]

            # If parentheses contain arguments, parse them
            arguments = parsed_line[parsed_line.find('(') + 1:parsed_line.find(')')]
            if arguments:
                arguments = arguments.partition(', ')

                instance_id = arguments[0].replace('\"', '')

                if arguments[2]:
                    if arguments[2][0] == '{' and arguments[2][-1] == '}':
                        args = arguments[2]
                    else:
                        args = arguments[2].replace(',', '')
                line = ' '.join([command, class_name, instance_id, args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, args):
        """Exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, args):
        """Handles EOF to exit program"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def check_value_type(self, value):
        """Checks the type of value"""
        arg = ""
        if value[0] == '"' and value[-1] == '"':
            for i in range(1, len(value) - 1):
                if value[i] == "_":
                    arg += " "
                    continue
                arg += value[i]
            return arg
        elif value.find(".") != -1:
            return float(value)
        else:
            return int(value)

    def do_create(self, args):
        """Create an object of any class"""
        arguments = args.split()
        if not args:
            print("** class name missing **")
            return
        elif arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arguments[0])()
        print(arguments[0])
        arguments.pop(0)
        for item in arguments:
            item = item.split('=')
            if len(item) != 2:
                continue
            key = item[0]
            value = item[1]
            value = self.check_value_type(value)
            if value is None:
                continue
            else:
                setattr(new_instance, key, value)
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Show an individual object"""
        new_args = args.partition(" ")
        class_name = new_args[0]
        instance_id = new_args[2]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = class_name + "." + instance_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object"""
        new_args = args.partition(" ")
        class_name = new_args[0]
        instance_id = new_args[2]
        if instance_id and ' ' in instance_id:
            instance_id = instance_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = class_name + "." + instance_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of)
