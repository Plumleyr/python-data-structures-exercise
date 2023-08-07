def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min_keys = ''
    max_keys = ''

    for k in d.keys():
        if min_keys == '' or k < min_keys:
            min_keys = k
        elif max_keys == '' or k > max_keys:
            max_keys = k
        
    return (min_keys, max_keys)
