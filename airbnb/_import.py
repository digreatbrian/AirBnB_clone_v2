#!/usr/bin/python3
""" module to import an object from str """


def _import(what: str):
    '''Import something absolutely with the relative path
    eg::
        _import("module.package.subpackage.Classname")
    '''
    if what.startswith("."):
        x = "Module shall not start with '.', Relative import not allowed"
        raise TypeError(x)
    if what.count(".") >= 1:
        item = what.split(".")[-1]
        if not item.strip():
            x = "Wrong import statement, module shall not end with '.'"
            raise TypeError(x)
        package = ''
        for p in what.split(".")[:what.count('.')]:
            x = '.' if not package.endswith('.') and package != '' else ''
            package += x
            package += p if p.strip() else '.'
        mod = __import__(package, globals(),
                         locals(), [package.split(".")[-1]])

        try:
            return getattr(mod, item)
        except Exception:
            err = f"module '{package}' has no definition for '{item}'"
            raise TypeError(err)
    else:
        mod = __import__(what, globals(), locals(), [])
        return mod
