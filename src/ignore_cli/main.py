import argparse
import os
from ignore_cli.gitignore_generator import generate_gitignore

# Handles the 'create' command to generate a .gitignore file
def handle_create_command(args):
    target_directory = os.path.abspath(args.directory)

    if not os.path.isdir(target_directory):
        print(f"Error: The specified directory '{target_directory}' does not exist.")
        return
    generate_gitignore(target_directory)

def main():
    # Parses arguments from the command line
    parser = argparse.ArgumentParser(
        description='Generate a .gitignore file in the specified directory.'
    )

    # Adds a subparser for the 'create' command
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Adds an argument to create a .gitignore file
    create_parser = subparsers.add_parser('create', help='Create a .gitignore file in the specified directory')

    # Adds an optional argument for the directory where the .gitignore file will be created
    create_parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='The directory where the .gitignore file will be created. Defaults to the current directory.'
    )

    # Sets the function to be called when the 'create' command is used
    create_parser.set_defaults(func=handle_create_command)

    args = parser.parse_args()

    # Calls the appropriate function based on the command provided
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()