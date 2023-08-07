def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    i = 0
    newstring = ''
    for letter in phrase:
        if i == 0 or phrase[i - 1] == ' ':
            newstring += phrase[i].upper()
            i += 1
        else:
            newstring += letter.lower()
            i += 1
    return newstring
