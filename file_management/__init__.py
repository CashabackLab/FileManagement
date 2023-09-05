#allows usage of the function from the package name directly
#i.e. file_management.varName()
__version__ = "0.4.8"

from .get_condition_data import * 
from .get_trial_table import * 
from .get_target_table import * 
from .create_folder import create_folder

from .varName import *
from .get_most_recent_file import get_most_recent_file
#from .nameof import nameof
from varname import nameof, argname
from .copyfolderstruct import *
from importlib import reload

from os.path import join, normpath, getctime, exists, abspath
from os import getcwd, mkdir, chdir

from .load_data import load_data
from .save_data import save_data
