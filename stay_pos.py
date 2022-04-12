def get_positive_numbers():
    return list(filter(lambda x: x > 0, list(map(int, input("Enter numbers: ").split(',')))))
