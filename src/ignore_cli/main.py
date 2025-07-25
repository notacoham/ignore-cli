import argparse
import os

DEFAULT_GITIGNORE_CONTENT = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.pyc
*.pyd
*.pyo

# Distribution / packaging
.Python
env/
venv/
*.egg
*.egg-info/
dist/
build/
*.whl

# IDE-specific files
.idea/             # IntelliJ / PyCharm
*.iml              # IntelliJ / PyCharm module files
.vscode/           # VS Code
.vscode-server/    # VS Code remote development
.history/          # Some IDEs' local history

# Operating System files
.DS_Store          # macOS
Thumbs.db          # Windows

# Temporary files, logs, etc.
*.log
*.tmp
*.bak

# Testing
.pytest_cache/
htmlcov/
.coverage

# User-specific configuration (if any sensitive data)
# .env # If you use python-dotenv for environment variables
"""

def generate_gitignore(directory, content=DEFAULT_GITIGNORE_CONTENT):
    gitignore_path = os.path.join(directory, '.gitignore')

    try:
        if os.path.exists(gitignore_path):
            print(f".gitignore file already exists at {gitignore_path}")
            return
        
        with open(gitignore_path, 'w') as f:
            f.write(content.strip())
        print(f".gitignore file created at {gitignore_path}")
    except IOError as e:
        print(f"Error creating .gitignore file: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Generate a .gitignore file in the specified directory.'
    )

    parser.add_argument(
        '--create',
        action='store_true',
        help='Create a .gitignore file in the specified directory.'
    )

    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='The directory where the .gitignore file will be created. Defaults to the current directory.'
    )

    args = parser.parse_args()

    if args.create:
        target_directory = os.path.abspath(args.directory)

        if not os.path.isdir(target_directory):
            print(f"Error: The specified directory '{target_directory}' does not exist.")
            return
        generate_gitignore(target_directory)
    else:
        print("No action specified.")
        print("Use --help for more information.")

if __name__ == '__main__':
    main()