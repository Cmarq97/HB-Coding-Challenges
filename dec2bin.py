import math
"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""
# 2^n-1 100 0+0+2^2=0+0+4
# 111 1+2+4=7


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    digits = int(math.log(num, 2)) + 1
    binary_value = ''
    for i in range(digits, 0):
        while (num - 2**(i-1)) >= 0:
            binary_value = binary_value + '1'
            num = num - 2**(i-1)
        binary_value = binary_value + '0'
    return binary_value


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
