
#!/usr/bin/python3
"""Module for printing a full name.

This module provides a function that prints:
"My name is <first name> <last name>"
with type validation on both names.
"""


def say_my_name(first_name, last_name=""):
    """Print a person's full name.

    Args:
        first_name: first name (must be a string).
        last_name: last name (must be a string, optional).

    Returns:
        None

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
