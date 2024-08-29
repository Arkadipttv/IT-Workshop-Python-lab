def move_duplicates_to_end(lst):
    duplicates=[]
    non_duplicates=[]
    """
    Move all duplicate values in a list to the end of the list.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list with duplicates at the end.
    """
    # Create a dictionary to store the count of each element
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Separate the list into two lists: one with duplicates and one without
    #non_duplicates = [num for num in lst if count_dict[num] == 1]
    for num in lst:
        if count_dict[num] == 1:
            non_duplicates.append(num)
    #duplicates = [num for num in lst if count_dict[num] > 1]
    
        if count_dict[num] > 1:
            duplicates.append(num)

    # Combine the two lists, with non-duplicates first
    result = non_duplicates + duplicates

    return result

# Test cases
print(move_duplicates_to_end([1, 2, 2, 3, 4]))  # [1, 3, 4, 2, 2]
print(move_duplicates_to_end([1, 1, 2, 2, 3, 3, 4]))  # [4, 1, 1, 2, 2, 3, 3]
print(move_duplicates_to_end([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]