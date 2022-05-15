import typing
from typing import Any, Generator


def my_filter(function_or_None: callable, iterable: typing.Iterable) -> Generator[Any, Any, None]:
    """
    :param function_or_None: function which allow us to do filter
    :param iterable: collection of items which we are checking
    :return: filtered item generator from the collection
    """
    return (item for item in iterable
            if (function_or_None(item) if function_or_None is not None else item))
