def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    reverse_vowel_string = ''
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    left_side_of_str = []
    right_side_of_str = []

    i = 0

    while i < (len(s) / 2):
        for letter in s:
            if letter in vowels:
                left_side_of_str.append(s[i])
                i += 1
            else:
                i += 1
                
    while i > len(s)/2 and i < len(s):
        for letter in s[i::]: 
            if letter in vowels:
                right_side_of_str.append(s[i])
                i += 1
            else:
                i += 1

    R = 0
    L = len(left_side_of_str) - 1
    for letter in s:
        if letter in vowels and R < len(right_side_of_str):
            reverse_vowel_string += right_side_of_str[R]
            R += 1
        elif letter in vowels and L > -1:
            reverse_vowel_string += left_side_of_str[L]
            L -= 1
        else:
            reverse_vowel_string += letter

    return reverse_vowel_string