#!/usr/bin/python3
def safe_function(fct,*args):
    import sys
    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return None
