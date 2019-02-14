import sys
import re
from collections import Counter

TEN_WORDS = 10


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as text_file:
            text = text_file.read()
            return text
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def get_clean_list_of_words(text):
    pattern = re.compile(r'[^a-zA-Zа-яА-Я\s]')
    clean_text = pattern.sub('', text).lower()
    list_of_words = re.split(r'\s+', clean_text)
    return list_of_words


def get_most_frequent_words(list_of_words):
    ten_most_frequent_words = Counter(list_of_words).most_common(TEN_WORDS)
    return ten_most_frequent_words


def print_most_frequent_words(ten_most_frequent_words):
    for frequency_dict in ten_most_frequent_words:
        print('The word "{0}" occurs {1} times'.format(frequency_dict[0], frequency_dict[1]))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('Usage: {0} + your_file.json'.format(sys.argv[0]))
        sys.exit()
    text = load_data(sys.argv[1])
    if text is None:
        sys.exit('No such file or decode error')
    ten_most_frequent_words = get_most_frequent_words(get_clean_list_of_words(text))
    print_most_frequent_words(ten_most_frequent_words)
