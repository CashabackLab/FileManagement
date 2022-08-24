import os

def create_folder(folder_name, path = ""):
    """
    Creates folder in current directory if it does not already exist. 
    Can optionally set path to create folder in a different directory.
    """
    path = os.path.normpath(path)
    full_path = os.path.join(path, folder_name)
    
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        
    return os.path.abspath(full_path)
