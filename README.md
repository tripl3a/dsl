# A Domain Specific Language (DSL) in Python

A simple DSL that lets our users easily get some work done 
by calling into a library of functions.
DSLs are powerful tools. They’re another way we can be creative and solve problems 
that make it easier for our users to get work done. 
From the user’s perspective, they’re just running “commands.” 
From our perspective, we get to leverage Python’s dynamic nature 
and its features and, in turn, reap the rewards of having all of the power 
of Python and its ecosystem available to us. 
For example, we can easily make changes to a library module or extend 
the library with new modules to expose new functionality using 
the standard library or 3rd party packages.

The following techniques were used to create this DSL:

* importlib.import_module(): dynamically import a module at runtime
* getattr(): get an object’s attribute/function (-> reflection)
* variable-length function arguments and keyword arguments (*args, **kwargs)
* converting a string to a different type


## Prerequisites

Python 3 needs to be installed.

## How to use

```
# get help:
python dsl.py help=module

# run dsl script file:
python dsl.py src.dsl
```

## Writing a script that executes commands of our DSL

A user has to specify the following to execute commands of our DSL:
* module name
* function name
* parameters, separated by whitespaces

see `src.dsl` as an example

## Acknowledgments

inspired by [Dan Bader's blog](https://dbader.org/blog/writing-a-dsl-with-python)


