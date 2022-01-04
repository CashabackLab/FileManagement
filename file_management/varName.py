def varName(p, name_space = globals()):
    """
    Return name of the variable as a string
    p: variable of any type
    """
    for k, v in name_space.items(): print(k)
    for k, v in name_space.items():
        if id(p) == id(v):
            return k
