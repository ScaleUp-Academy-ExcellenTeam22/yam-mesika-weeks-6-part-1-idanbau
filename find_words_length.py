def words_length(sentence: str):
    """
    :param sentence: check for words length
    :return: each length for words in the list
    """
    words_list = sentence.split()
    return [len(word) for word in words_list]
