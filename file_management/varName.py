def varName(p, name_space = globals()):
    """
    Return name of the variable as a string
    p: variable of any type
    name_space: namespace of the variable to use
    NOTE: must specify name_space = globals() when calling the function, should not be omitted
    """
    for k, v in name_space.items():
        if id(p) == id(v):
            return k
