# In a given text you need to sum the numbers. Only separated numbers should be counted. 
# If a number is part of a word it shouldn't be counted.

# The text consists of numbers, spaces and English letters.

# Input: A string.
# Output: An int.

def sum_numbers(text: str) -> int:
    result = 0
    for i in text.split():
        if i.isdigit():
            result += int(i)
    return result

        

if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi 5'))
    print(sum_numbers('hi4'))
    print(sum_numbers('hi 4 10'))
    

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Done!")