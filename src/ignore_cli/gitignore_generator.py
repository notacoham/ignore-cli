import os

# Default content for the .gitignore file
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
    # Sets the path for the .gitignore file
    gitignore_path = os.path.join(directory, '.gitignore')

    try:
        # Checks if the .gitignore file already exists
        if os.path.exists(gitignore_path):
            print(f".gitignore file already exists at {gitignore_path}")
            return
        
        # Writes the default content to the .gitignore file
        with open(gitignore_path, 'w') as f:
            f.write(content.strip())
        print(f".gitignore file created at {gitignore_path}")
    except IOError as e:
        print(f"Error creating .gitignore file: {e}")