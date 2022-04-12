import filter
import stay_pos
import find_words_length
# import get_alphabetic_letters
import get_full_names

# x = list(filter.my_filter(None, [True, False, True, True]))
# print(x)
# print(stay_pos.get_positive_numbers())

# print(find_words_length.words_length("Toto, I've a feeling we're not in Kansas anymore"))
# get_alphabetic_letters.get_letters()

first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']

print(get_full_names.full_names(first_names, last_names, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])