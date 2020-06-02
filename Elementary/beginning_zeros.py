# You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

# Input: A string, that consist of digits.

# Output: An Int.

# Precondition: 0-9


def beginning_zeros(number: str) -> int:
    digits = [int(x) for x in str(number)]
    result = 0
    for i in digits:
       if i == 0:
           result += 1
       elif i != 0:
           return result
    return result
 


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Done!")