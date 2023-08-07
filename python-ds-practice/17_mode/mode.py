def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest_val = 0
    dict_of_nums = {}
    for num in nums:
        dict_of_nums[num] = dict_of_nums.get(num, 0) + 1
    for value in dict_of_nums.values():
        if value > highest_val:
            highest_val = value
    for key, value in dict_of_nums.items():
        if value == highest_val:
            return key