def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict_of_num1 = {}
    dict_of_num2 = {}

    for num in str(num1):
        dict_of_num1[num] = dict_of_num1.get(num, 0)+1

    for num in str(num2):
        dict_of_num2[num] = dict_of_num2.get(num, 0)+1

    if dict_of_num1 == dict_of_num2:
        return True
    else:
        return False

    