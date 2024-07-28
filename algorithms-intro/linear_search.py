# linear search
def linear_search(list, target): #function definition
    """
    Perform a linear search on a list to find the index position of a target element.
    @param list - The list to search through.
    @param target - The element to find in the list.
    @return The index position of the target if found, otherwise None.
    """
    for i in range(0, len(list)): 
        if list[i] == target:
            return i
    return None

def verify(index): 
    """
    Perform a linear search on a list of numbers to find a target value.
    @param index - the target value to search for
    @return the index of the target value if found, None otherwise
    """
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers , 12) 
verify(result)

result = linear_search(numbers , 6) 
verify(result)
