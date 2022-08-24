#allows usage of the function from the package name directly
#i.e. file_management.varName()
__version__ = "0.4.2"

from .get_condition_data import * 
from .get_trial_table import * 
from .get_target_table import * 
from .create_folder import create_folder

from .varName import *
from .fileio import *
#from .nameof import nameof
from varname import nameof, argname
from .copyfolderstruct import *
from importlib import reload

