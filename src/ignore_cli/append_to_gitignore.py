import os

def append_to_gitignore(directory, pattern):
    gitignore_path = os.path.join(directory, '.gitignore')

    if not os.path.exists(gitignore_path):
        print(f"No .gitignore file found in {directory}. Trying to create one with 'create'.")
        return
    try:
        with open(gitignore_path, 'a') as f:
            f.write(f"\n{pattern}\n")
        print(f"Added '{pattern}' to {gitignore_path}")
    except IOError as e:
        print(f"Error writing to .gitignore file: {e}")