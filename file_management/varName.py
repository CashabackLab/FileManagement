#This function is legacy code kept for compatability. U
def varName(p, name_space = None):
    """
    LEGACY CODE. Use file_management.nameof instead
    
    Return name of the variable as a string
    p: variable of any type
    name_space: namespace of the variable to use
    NOTE: must specify name_space = globals() when calling the function, should not be omitted
    """
    if name_space == None:
        raise ValueError("Must set name_space = globals()")
        
    for k, v in name_space.items():
        if id(p) == id(v):
            return k
