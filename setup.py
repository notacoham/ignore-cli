import os
from setuptools import setup, find_packages

setup(
    name='ignore-cli',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'ignore = ignore_cli.main:main',
        ],
    },
    author='Alex Cottam',
    author_email='alexcottam12@gmail.com',
    description='A CLI tool to generate .gitignore files',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/notacoham/ignore-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)