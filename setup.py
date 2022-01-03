from setuptools import setup

setup(
    # Needed to silence warnings 
    name='FileManagement',
    url='https://github.com/CashabackLab/FileManagement',
    author='CashabackLab',
    author_email='cashabacklab@gmail.com',
    # Needed to actually package something
    packages=['varName', 'fileio'],
    # Needed for dependencies
    install_requires=['numpy', 'pickle'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='UD',
    description='Python package for managing file input/output and file saving, tailored for the Cashaback Lab',
    long_description=open('README.md').read(),
)
