def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    capitalized = ""

    capitalized += phrase[:1].upper()

    for char in phrase[1:]:
        capitalized += char

    return capitalized
