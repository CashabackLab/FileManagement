#allows usage of the function from the package name directly
#i.e. file_management.varName()
from .get_condition_data import * 
from .get_trial_table import * 
from .get_target_table import * 

from .varName import *
from .fileio import *
#from .nameof import nameof
from varname import nameof, argname
from .copyfolderstruct import *
from importlib import reload

