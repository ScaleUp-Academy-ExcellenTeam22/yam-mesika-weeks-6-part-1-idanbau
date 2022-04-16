def get_letters():
    """
    :return: list of all lower case letters and upper case
    """
    lower_case = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    upper_case = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
    return lower_case, upper_case
