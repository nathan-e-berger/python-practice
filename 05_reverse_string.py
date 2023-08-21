def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    characters = list(phrase)
    characters.reverse()
    reversed = str()
    for el in characters:
        reversed += el
    return reversed









    # reversed = list(phrase).reverse(reversed).join(reversed)


