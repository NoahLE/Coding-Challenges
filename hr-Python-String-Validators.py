def check_string_type(s):
    # Print true if the string contains any of the following characters
    contains_alphanumeric = False
    contains_alpha = False
    contains_digits = False
    contains_lowercase = False
    contains_uppercase = False

    for char in s:
        # If string alphanumeric
        if char.isalpha():
            contains_alphanumeric = True

        # If string is only alphabetical
        if char.isalpha():
            contains_alpha = True

        # If string is only digits
        if char.isnumeric():
            contains_digits = True

        # If string is all lowercase
        if char.islower():
            contains_lowercase = True

        # If string is all uppercase
        if char.isupper():
            contains_uppercase = True

    print(contains_alphanumeric)
    print(contains_alpha)
    print(contains_digits)
    print(contains_lowercase)
    print(contains_uppercase)


if __name__ == '__main__':
    # s = input()
    # fails on 123
    s = 123
    check_string_type(s)
