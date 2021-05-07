"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

# want to split phrase into list of separate strings
# then loop over list of strings, counting the number of times each word was seen
# can then place them in a dicitonary, key = word, value = number of times it's in phrase
# want to return that dictionary

    sep_phrase = phrase.split(" ")
    word_count = 0
    
    for words in sep_phrase:
        if words == words:
            word_count += 1
            word_list = []
            word_list.append(words)
            word_dict = dict(word_list, word_count)
            print(word_dict)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
