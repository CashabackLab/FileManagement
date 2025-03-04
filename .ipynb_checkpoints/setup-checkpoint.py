from setuptools import setup
import re
import ast

#Only change __version__ in file_management/__init__.py file
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('file_management/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))
setup(
    # Needed to silence warnings 
    name='FileManagement',
    url='https://github.com/CashabackLab/FileManagement',
    author='CashabackLab',
    author_email='cashabacklab@gmail.com',
    # Needed to actually package something
    packages=['file_management'],
    # Needed for dependencies
    install_requires=['numpy', 'varname'],
    # *strongly* suggested for sharing
    version=version,
    # The license can be anything you like
    license='MIT',
    description='Python package for managing file input/output and file saving, tailored for the Cashaback Lab',
    long_description=open('README.md').read(),
)
