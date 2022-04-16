def my_filter(function_or_None, iterable):
    """
    :param function_or_None: function which allow us to do filter
    :param iterable: collection of items which we are checking
    :return: filtered item generator from the collection
    """
    return (item for item in iterable
            if (function_or_None(item) if function_or_None is not None else item))
