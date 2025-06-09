import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [name for name, member in inspect.getmembers(mod) if inspect.isclass(member) and name[0].isupper()]