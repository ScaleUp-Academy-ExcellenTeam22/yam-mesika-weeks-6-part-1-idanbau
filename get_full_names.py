def full_names(first_names: [str], last_names: [str], min_length: int = 0):
    """
    :param first_names:list of first names
    :param last_names:list of last names
    :param min_length:minimum length of full name to take
    :return: list of all first name combinations with last names
    """
    return [f"{first_name.capitalize()} {last_name.capitalize()}"
            for first_name in first_names for last_name in last_names if
            len(f"{first_name} {last_name}") >= min_length]
