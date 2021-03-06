"""Sum a list of integers.

Given a list of numbers, return the sum. Do not use the built in 'sum' method.

For example::

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

The sum of an empty list is zero::

    >>> sum_list([])
    0

"""


def sum_list(num_list):
    """Return the sum of all numbers in list."""
    # return sum(num_list)
    sum_list = 0
    for number in num_list:
            sum_list += number
            print(sum_list)
    
        # code prints out the sum_list for each value, increasing by the value each time
        # final output is the sum of numbers
        # currently no output for '[]' as input 

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. BOOYA!!\n")
