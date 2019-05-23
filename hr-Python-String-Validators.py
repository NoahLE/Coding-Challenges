def StringValidator(VString):
    # --- print True of the string contains any of the following characters, otherwise, print False ---
    isAlphaNum = False
    isAlpha = False
    isDigit = False
    isLower = False
    isUpper = False

    for character in VString:
        # True if alphanumeric
        if character.isalnum():
            isAlphaNum = True

        # True if alphabetical
        if character.isalpha():
            isAlpha = True

        # True if digits
        if character.isdigit():
            isDigit = True

        # True if lowercase
        if character.islower():
            isLower = True

        # True if uppercase
        if character.isupper():
            isUpper = True

    print(f'{isAlphaNum} \n{isAlpha} \n{isDigit} \n{isLower} \n{isUpper}')

    pass

if __name__ == "__main__":
    s = input()
    StringValidator(s)
