import re


def words_from_file(filename):
    """ Returns a list of words from the given file.
    Don't worry about how.
    The file needs to exist :)
    Students should call this from their function to
    get the list of words from a file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read().lower()
        words = re.findall('[a-zA-Z]+', raw_data)
    return words


def print_word_counts(filename):
    """Print the counts of all words in the given file, in alphabetical order.
       The file is loaded using the words_from_file function.
    """
    words = words_from_file(filename)
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")