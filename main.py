import filter
import get_alphabetic_letters
import stay_pos
import find_words_length
import get_full_names
import get_words_count

if __name__ == "__main__":
    x = list(filter.my_filter(None, [True, False, True, True]))
    print(x)
    print(stay_pos.get_positive_numbers())

    print(find_words_length.words_length("Toto, I've a feeling we're not in Kansas anymore"))
    get_alphabetic_letters.get_letters()

    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(get_full_names.full_names(first_names, last_names, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi',
                                                                     'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi',
                                                                     'Yaakov Mizrahi'])

    print(get_words_count.count_words("""
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """))
