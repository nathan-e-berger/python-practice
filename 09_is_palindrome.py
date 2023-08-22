def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')

    first = 0
    last = len(phrase) - 1

    while (first < last):
        if phrase[first] != phrase[last]:
            return False
        else:
            first += 1
            last -= 1
    return True
