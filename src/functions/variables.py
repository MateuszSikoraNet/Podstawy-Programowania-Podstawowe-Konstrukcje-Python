def swap(a, b):
    # Return the values in reverse order.
    pass


def increment(value, amount=1):
    # Add amount to value.
    pass


def decrement(value, amount=1):
    # Subtract amount from value.
    pass


def accumulate(values):
    # Add all values.
    pass


def get_default_values():
    # Return the default name, age, and active values.
    pass


def chained_assignment():
    # Do a = b = [], then a.append(1), then return b.
    # Chained assignment binds both names to ONE object, so b sees the change.
    pass


def is_valid_name(name):
    # Return True if name can be used as a variable name: it must be an identifier
    # (letters, digits and _, not starting with a digit - name.isidentifier())
    # and must not be a Python keyword such as "class" or "for" (keyword.iskeyword(name)).
    pass


def delete_variable():
    # Do x = 1, then del x, then return x.
    # del removes the name, so reading it afterwards raises NameError (UnboundLocalError inside a function).
    pass
