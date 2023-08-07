def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    capitalized_first_letter_string = phrase[0].upper() + phrase[1:]
    return capitalized_first_letter_string