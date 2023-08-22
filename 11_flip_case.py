def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # swapcase() method
    word = ''
    swap_chars = to_swap.upper() + to_swap.lower()

    for char in phrase:
        if char.islower() and char in swap_chars:
            word += char.upper()
        elif char.isupper() and char in swap_chars:
            word += char.lower()
        else:
            word += char
    return word
