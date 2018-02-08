"""
A module for adding objects.
"""

def add_str(*args, **kwargs):
    """
    Concatenates all arguments as strings. Prints results to stdout.
    Keywords arguments are being appended at the end, separated by comma.
    """
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    joined_args = ''.join(args)
    joined_kwargs = ','.join(kwargs_list)
    if joined_args != "" and joined_kwargs != "":
        joined_args = joined_args + ","
    print(joined_args + joined_kwargs)

def add_num(*args, **kwargs):
    """
    Adds all arguments as numbers of type int or float. Prints results to stdout.
    You have to specify "type=int" or "type=float" as last argument.
    """
    t = globals()['__builtins__'][kwargs['type']]
    print(sum(map(t, args)))
