import argparse
import os
from ignore_cli.gitignore_generator import generate_gitignore
from ignore_cli.append_to_gitignore import append_to_gitignore
from ignore_cli.scan_for_gitignore import scan_directory
from ignore_cli.process_gitignore import generate_gitignore as process_generate_gitignore

# Handles the 'create' command to generate a .gitignore file
def handle_create_command(args):
    target_directory = os.path.abspath(args.directory)

    if not os.path.isdir(target_directory):
        print(f"Error: The specified directory '{target_directory}' does not exist.")
        return
    # Scans the directory for existing .gitignore files
    combined_files_and_dirs = scan_directory(target_directory)
    

    # generate_gitignore(target_directory)

# Handles the 'add' command to add to a gitignore file
def handle_add_command(args):
    target_directory = os.path.abspath(args.directory)
    pattern_to_add = args.pattern

    if not os.path.isdir(target_directory):
        print(f"Error: The specified directory '{target_directory}' does not exist.")
        return
    append_to_gitignore(target_directory, pattern_to_add)

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

    # Adds an argument to add a pattern to the .gitignore file
    add_parser = subparsers.add_parser('add', help='Add a pattern to the .gitignore file in the specified directory')
    add_parser.add_argument(
        '--directory',
        default='.',
        help='The directory where the .gitignore file is located. Defaults to the current directory.'
    )
    add_parser.add_argument(
        'pattern',
        help='The pattern to add to the .gitignore file.'
    )
    add_parser.set_defaults(func=handle_add_command)

    args = parser.parse_args()

    # Calls the appropriate function based on the command provided
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()