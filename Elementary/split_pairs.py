# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

# Input: A string.

# Output: An iterable of strings.

# Precondition: 0<=len(str)<=100


def split_pairs(a):
    if len(a) % 2 ==0:
        array = [a[i:i+2] for i in range(0, len(a), 2)]
    else:
        array = [a[i:i+2] for i in range (0, len(a)-1,2) ]
        array.append(a[-1]+"_")
    return array


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abc')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Done!")