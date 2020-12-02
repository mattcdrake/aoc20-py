def is_valid_password(lower: int, upper: int, string: str, char: str) -> bool:
    """
    Determines whether a string contains a given character within the specified
    range.
    """
    # XOR
    return (string[lower-1] == char) != (string[upper-1] == char)


def count_chars(string: str, char: str) -> int:
    """
    Counts the number of times a character appears in a string.
    """
    found_char = 0
    for letter in string:
        if char == letter:
            found_char += 1

    return found_char


def get_bounds(bound_str: str) -> (int, int):
    """
    Returns (int, int) where 0 is the lower bound and 1 is the upper bound.

    Expects strings of the form "[int]-[int]"
    """
    nums = bound_str.split('-')
    return (int(nums[0]), int(nums[1]))


def p_1(input_path: str) -> str:
    with open(input_path) as f:
        lines = [line for line in f.readlines()]

    valid_passwords = 0

    for line in lines:
        parts = line.split()
        lower, upper = get_bounds(parts[0])
        found_ct = count_chars(parts[2], parts[1][0])

        if found_ct >= lower and found_ct <= upper:
            valid_passwords += 1

    return str(valid_passwords)


def p_2(input_path: str) -> str:
    with open(input_path) as f:
        lines = [line for line in f.readlines()]

    valid_passwords = 0

    for line in lines:
        parts = line.split()
        lower, upper = get_bounds(parts[0])

        if is_valid_password(lower, upper, parts[2], parts[1][0]):
            valid_passwords += 1

    return str(valid_passwords)

