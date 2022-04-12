def my_filter(function_or_None, iterable):
    return (item for item in iterable if (function_or_None(item) if function_or_None is not None else item))