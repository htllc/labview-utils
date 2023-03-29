import importlib.util

__version__ = '0.1.0'

def get_module_path(module_name):
	return importlib.util.find_spec(module_name).origin
