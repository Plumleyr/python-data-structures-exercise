def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    
    count = (len(parens)/2)
    i = 0
    j = (len(parens) - 1)

    if len(parens) % 2 != 0:
        return False

    if parens[0] != '(':
        return False

    while count > 0:
        if parens[i] == parens[j]:
            return False
        else:
            count -= 1
            i += 1
            j -= 1
    
    return True
        

