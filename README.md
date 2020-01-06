# pdoc3-problem-example

This repository illustrates unexpected behavior with the `pdoc3` documentation tool.

## The Problem

Including a section header in the module-level docstring which matches a class name
disrupts parsing the class source code and prevents its inclusion in the rendered HTML.

The package in this example is a simple contrived example that makes this behavior obvious:

```
./
└── some_package
    ├── error1.py
    ├── error2.py
    └── __init__.py
```

In this example, the only difference between `error1.py` and `error2.py` is `error1.py` has

```
class `Error`
-------------
```

in the module docstring while `error2.py` has just

```
class Error
-----------
```

This is certainly not something you would expect and not something the error

```
~/.local/lib/python3.6/site-packages/pdoc/__init__.py:227: UserWarning: Couldn't get/parse source of '<Class 'some_package.error2.Error'>'
  warn("Couldn't get/parse source of '{!r}'".format(doc_obj))
```

makes clear is happening.

