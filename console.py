#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """display prompt """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

    def do_EOF(self, line):
        """Exits the console when 'EOF' is entered"""
        print()
        return True

    def do_quit(self, line):
        """Exits the console when 'quit' is entered"""
        return True

    def help_quit(self, arg):
        """Displays the help message for the 'quit' command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """
        do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg=None):
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])
    
    def do_destroy(self, arg):
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()
        
    def do_all(self, arg):
        arg_list = parse(arg)
        if len(
            arg_list) > 0 and arg_list[0] \
                not in HBNBCommand.classes:
                    print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)

    def do_update(self, arg):
        """instance's attribute updated"""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            instance = obj_dict[key]
            setattr(instance, arg_list[2], arg_list[3].strip('"'))
            storage.save()
            
def parse(arg):
    """Convert a series arguments to an argument list"""
    return list(map(str, arg.split()))
      
        

if __name__ == '__main__':
    """Initializes the command line interface and starts the loop"""
    HBNBCommand().cmdloop()
