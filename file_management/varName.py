def varName(p):
    """
    Return name of the variable as a string
    p: variable of any type
    """
    temp_global = globals()
    for k, v in temp_global: print(k)
    for k, v in temp_global.items():
        if id(p) == id(v):
            return k
