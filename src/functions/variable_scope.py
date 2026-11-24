GLOBAL_VALUE = 10
_counter = 0


def increment_counter():
    # Add one to the global counter.
    # Return the global counter.
    pass


def get_counter():
    # Return the global counter.
    pass


def reset_counter():
    # Set the global counter to zero.
    pass


def set_local_value(value):
    # Set a local value without changing GLOBAL_VALUE.
    pass


def get_global_value():
    # Return GLOBAL_VALUE.
    pass


def make_counter(start=0):
    # Return a function that adds one to a saved value each time.
    pass


def make_multiplier(factor):
    # Return a function that multiplies a value by factor.
    pass


def try_increment_without_global():
    # Do "_counter += 1" WITHOUT the global statement.
    # Assigning to a name anywhere in a function makes it local in the whole function,
    # so reading it first raises UnboundLocalError.
    pass


def last_loop_value(values):
    # Return the loop variable after "for value in values" has finished, or None if values is empty.
    # values can be any iterable (list, tuple, string, dict, iterator) - use the loop, not indexing.
    # Python has no block scope: a variable created inside a for/if block still exists after it.
    pass


def comprehension_variable():
    # Set x = "outer", then build [x for x in range(3)], then return x.
    # A comprehension has its own scope, so its x does not overwrite the outer x.
    pass


def shadowed_builtin(values):
    # Assign max = 100 in this function, then return max(values).
    # The local name hides the built-in max(), so calling it raises TypeError (an int is not callable).
    pass


def make_counter_without_nonlocal():
    # Return an inner function that does "count += 1" on count = 0 from this function, WITHOUT nonlocal.
    # Assigning makes count local to the inner function, so calling it raises UnboundLocalError
    # (compare make_counter, which needs nonlocal to change the enclosing variable).
    pass


def count_locally():
    # Set count = 0, add 1, return count.
    # A local variable is created anew on every call, so this always returns 1 (compare make_counter).
    pass


def make_adders_late_binding(count):
    # Return [lambda x: x + i for i in range(count)].
    # Each lambda looks up i when it is called, not when it is created, so all of them use the last i.
    pass


def make_adders(count):
    # Return count functions; the n-th one adds n to its argument.
    # Freeze the current i in each lambda with a default argument: lambda x, i=i: x + i.
    pass
