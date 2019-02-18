import sys
import re
from collections import Counter


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as text_file:
            text = text_file.read()
            return text
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def get_clean_list_of_words(text):
    clean_text = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', text).lower()
    list_of_words = re.split(r'\s+', clean_text)
    return list_of_words


def get_most_frequent_words(list_of_words, word_count = 10):
    most_frequent_words = Counter(list_of_words).most_common(word_count)
    return most_frequent_words


def print_most_frequent_words(most_frequent_words):
    for frequency_tuple in most_frequent_words:
        print('The word "{0}" occurs {1} times'.format(*frequency_tuple))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('Usage: {0} + your_file.json'.format(sys.argv[0]))
        sys.exit()
    text = load_data(sys.argv[1])
    if text is None:
        sys.exit('No such file or decode error')
    most_frequent_words = get_most_frequent_words(get_clean_list_of_words(text))
    print_most_frequent_words(most_frequent_words)
