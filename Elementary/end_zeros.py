# Try to find out how many zeros a given number has at the end.

# Input: A positive Int

# Output: An Int.


def end_zeros(num: int) -> int:
    digits = [int(x) for x in str(num)]
    result = 0
    for i in digits[::-1]:
       if i == 0:
           result += 1
       elif i != 0:
           return result
    return result
        

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(11100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Done!")