from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""

    words = None
    with open(DICTIONARY, 'r') as f:
        words = [line.strip() for line in f]

    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum([LETTER_SCORES.get(c.upper(), 0) for c in word])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    return max(words or load_words(), key=lambda word: calc_word_value(word))


if __name__ == "__main__":
    pass    # run unittests to validate
