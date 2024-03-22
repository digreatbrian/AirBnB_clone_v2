#!/usr/bin/python3
""" module to import an object from str """


def _import(what: str):
    '''Import something absolutely with the relative path
    eg::
        _import("module.package.subpackage.Classname")'''
    
    if what.startswith("."):
        raise TypeError("Module shall not start with '.', Relative import not allowed")
    if what.count(".") >= 1:
        item = what.split(".")[-1]
        if not item.strip():
            raise TypeError("Wrong import statement, what you want to import shall not end with '.'")
        package = ''
        for p in what.split(".")[:what.count('.')]:
            package += '.' if not package.endswith('.') and package != '' else ''
            package += p if p.strip() else  '.'
        mod = __import__(package, globals(), locals(), [package.split(".")[-1]])

        try:
            return getattr(mod, item)
        except:
            raise TypeError(f"module '{package}' has no definition for '{item}'")
    else:
        mod = __import__(what, globals(), locals(), [])
        return mod

