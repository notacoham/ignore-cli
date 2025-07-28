import os
import fnmatch

# gitignore patterns dictionary
gitignore_patterns = {
    "directories": [
        "__pycache__", ".Python", "build", "dist", "wheels", ".tox", ".mypy_cache",
        "build-*", "dist-*", ".app", 
        "venv", "env", ".venv", ".env", "pyvenv", "envs", ".conda", ".condatmp",
        ".poetry", ".hatch",
        ".vscode", ".vscode-server", ".vscode-test", ".idea", ".project", ".metadata",
        ".atom", "auto-save-list", "tramp", ".settings", "nbproject", ".gproject",
        ".kateproject",
        ".DS_Store", ".AppleDouble", ".Trashes", ".Spotlight-V100", ".TemporaryItems",
        ".fseventsd", "$RECYCLE.BIN", "System Volume Information",
        ".ipynb_checkpoints", "data", "models", "checkpoints", "runs", "logs", "results",
        "outputs", ".tensorboard-info", ".dvc/cache",
        "logs", "log", "tmp", "temp", "output",
        ".secrets", ".local", ".config",
        ".aws-sam", ".serverless", ".firebase", ".render", ".heroku", ".vercel", ".next",
        "node_modules", ".pnp", ".yarn",
        "docs/_build", ".remote",
    ],
    "file_extensions": [
        "pyc", "pyd", "pyo", "so", "lo", "dylib", "egg", "whl", "c", "cpp", "f", "for",
        "ftn", "f90", "f95", "f03", "f08", "pxd", "pyx", "dll", "exe", "manifest", "bin", "out",
        "iml", "iws", "sublime-project", "sublime-workspace", "swp", "swo", "swn",
        "bak", "tmp", "elc", "suo", "user", "ncb", "aps", "pdb", "obj", "sbr", "bsc",
        "res", "pch", "lib", "exp", "ilk", "msi", "msp",
        "csv", "tsv", "dat", "hdf5", "h5", "feather", "parquet", "json", "geojson", "xml",
        "yml", "yaml", "sqlite", "db", "mdb", "accdb", "xls", "xlsx", "xlsm", "jpg",
        "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "mp4", "avi", "mov", "mkv",
        "mp3", "wav", "flac", "pkl", "pickle", "npy", "npz", "bin", "weights", "tf",
        "ckpt", "onnx", "pb", "pth", "pt", "keras", "cbm", "dill",
        "log", 
        "terraform.tfvars", "key", "pem", "crt", "csr", "pfx", "sqlite3", "db3",
        "db-journal", "db-wal", "db-shm",
    ],
    "specific_files": [
        ".LSOverride", "Thumbs.db", "desktop.ini", "._*",
        "Pipfile.lock", "poetry.lock",
        "*.tmp", 
        "*.orig", "*.rej", "*.diff", "*.patch", 
        "*~", "#*#", ".#*", "%*", 
        ".env", ".env.local", ".flaskenv", "config.ini.local",
        "settings_local.py", "local_settings.py",
        "npm-debug.log", "yarn-debug.log", "yarn-error.log", ".pnp.js",
        "Dockerfile.backup",
    ],
    "generic_wildcard_patterns": [
        "npm-debug.log*", 
        "yarn-debug.log*",
        "yarn-error.log*",
        ".coverage", 
        ".coverage.*",
    ]
}

# file and directory scanning function
def scan_directory(directory='.', command=None):
    # Variable to hold the root directory and initialize sets for files and directories
    root_directory = os.path.abspath(directory)
    all_files = set()
    all_dirs = set()
    combined_files_and_dirs = {}
    gitignore_files_and_dirs = {}

    # Walk through the directory tree using os.walk
    print(f"Scanning directory: {root_directory}")
    for root, dirs, files in os.walk(root_directory):
        # Loop through files searching endings for extensions and specific files
        for file in files:
            file_ending = file.split('.')[-1] if '.' in file else ''
            if file_ending in gitignore_patterns["file_extensions"]:
                file_ending = f".{file_ending}"
                all_files.add(file_ending)
            if file in gitignore_patterns["specific_files"]:
                file_ending = f".{file_ending}"
                all_files.add(file_ending)
            # loop through generic wildcard patterns and check if file matches
            for pattern in gitignore_patterns["generic_wildcard_patterns"]:
                # Use fnmatch to match patterns
                if fnmatch.fnmatch(file, pattern):
                    file_ending = f".{file_ending}"
                    all_files.add(file_ending)

        # Check if the directory matches any patterns in gitignore_patterns
        for dir in dirs:
            if dir in gitignore_patterns["directories"]:
                dir = f"{dir}/"
                all_dirs.add(dir)
            for pattern in gitignore_patterns["generic_wildcard_patterns"]:
                # Use fnmatch to match patterns
                if fnmatch.fnmatch(dir, pattern):
                    dir = f"{dir}/"
                    all_dirs.add(dir)

        # If the command is 'add', scan the gitignore file for existing patterns
        if command == 'add':
            gitignore_path = os.path.join(directory, '.gitignore')
            with open(gitignore_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '/' in line: 
                            gitignore_files_and_dirs.setdefault('directories', []).append(line)
                        else:
                            gitignore_files_and_dirs.setdefault('files', []).append(line)

        
    
    # Loop through all files and directories to add them to combined_files_and_dirs
    for file in all_files:
        if combined_files_and_dirs.get('files') is None:
            combined_files_and_dirs['files'] = []
        combined_files_and_dirs['files'].append(file)
    for dir in all_dirs:
        if combined_files_and_dirs.get('directories') is None:
            combined_files_and_dirs['directories'] = []
        combined_files_and_dirs['directories'].append(dir)
    # print(f"Combined Files and Directories: {combined_files_and_dirs}")

    # If the command is 'add', combine both dictionaries into one and return it
    if command == 'add':
        combined_dict = {}
        combined_dict['files'] = list(set(gitignore_files_and_dirs.get('files', []) + combined_files_and_dirs.get('files', [])))
        combined_dict['directories'] = list(set(gitignore_files_and_dirs.get('directories', []) + combined_files_and_dirs.get('directories', [])))
        # print(f"Combined files and directories: {combined_dict}")
        return combined_dict

    # print(f"Files: {all_files}")
    # print("" + "-" * 80)
    # print(f"Directories: {all_dirs}")
    # print("" + "-" * 80)
    # print(f"Combined Files and Directories: {combined_files_and_dirs}")
    return combined_files_and_dirs
