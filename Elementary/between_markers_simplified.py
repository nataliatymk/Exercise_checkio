# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

# This is a simplified version of the Between Markers mission.

# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

# Output: A string.


# def between_markers(text: str, begin: str, end: str) -> str:
#     if text.startswith(begin):
#         for t in text.split(end):
#             if t.startswith(begin):
#                 return t[1:]
#     else:
#         for t in text.split(begin):
#             if t.endswith(end):
#                 return t[:-1]

def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1:text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("[an apple]","[","]"))
    print(between_markers(">Apple< is simple",">","<"))
    print(between_markers('>apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Done!')
