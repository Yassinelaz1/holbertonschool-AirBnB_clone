#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """display prompt """
    prompt = "(hbnb) "


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

if __name__ == '__main__':
    """Initializes the command line interface and starts the loop"""
    HBNBCommand().cmdloop()
