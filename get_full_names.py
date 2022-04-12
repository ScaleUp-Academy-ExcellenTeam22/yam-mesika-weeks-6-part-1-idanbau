def full_names(first_names: [str], last_names: [str], min_length: int = 0):
    return [f"{first_name.capitalize()} {last_name.capitalize()}"
            for first_name in first_names for last_name in last_names if
            len(f"{first_name} {last_name}") >= min_length]
