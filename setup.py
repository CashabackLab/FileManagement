from setuptools import setup

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
    version='0.2.6',
    # The license can be anything you like
    license='MIT',
    description='Python package for managing file input/output and file saving, tailored for the Cashaback Lab',
    long_description=open('README.md').read(),
)
