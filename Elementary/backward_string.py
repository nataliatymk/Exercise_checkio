# You should return a given string in reverse order.

# Input: A string.

# Output: A string.

def backward_string(val: str) -> str:
    reverse_str = val[::-1]
    return reverse_str


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Done!")