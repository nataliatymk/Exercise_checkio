# In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

# Input: List.

# Output: Iterable.


from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        new_list = items[1:]
        new_list.append(items[0])
        return new_list
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Done!")