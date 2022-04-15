import importlib

def reloadpackage(package_name):
  """
  Alias for importlib.reload()
  """
  importlib.reload(package_name)
