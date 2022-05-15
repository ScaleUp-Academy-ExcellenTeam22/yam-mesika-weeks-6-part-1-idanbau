def words_length(sentence: str) -> list:
    """
    :param sentence: The sentence to check for words length
    :return: List of words length
    """
    words_list = sentence.split()
    return [len(word) for word in words_list]
