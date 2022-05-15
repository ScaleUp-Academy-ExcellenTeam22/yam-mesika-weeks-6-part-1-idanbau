import string


def count_words(text: str) -> dict:
    """
    :param text: full text to check for words length
    :return: map of words list and their length
    """
    formatted_text = set(filter(lambda x: len(x) > 0,
                                [''.join([character for character in word if character in string.ascii_letters]).lower()
                                 for word in text.split()]))
    return {word: len(word) for word in formatted_text}
