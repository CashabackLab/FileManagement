import dill

def load_data(file, *args, **kwargs):
    with open(file, "rb") as f:
        return dill.load(f, *args, **kwargs)
    
