import dill

def save_data(data, file, *args, **kwargs):
    with open(file, "wb") as f:
        return dill.dump(data, f, *args, **kwargs)
