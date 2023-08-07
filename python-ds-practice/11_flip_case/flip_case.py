def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newstring = ''
    for letter in phrase:
        if letter == to_swap.upper():
           newstring += letter.lower()
        elif letter == to_swap.lower():
            newstring += letter.upper()
        else:
            newstring += letter

    return newstring