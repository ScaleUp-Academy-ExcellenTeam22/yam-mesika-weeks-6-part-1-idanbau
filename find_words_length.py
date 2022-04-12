def words_length(sentence: str):
    words_list = sentence.split()
    return [len(word) for word in words_list]