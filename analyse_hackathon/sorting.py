def bubble_sort(items):
    """

    Return array of items, sorted in ascending order using bubble sort method.

    Args:
        items (array): list of array-like object of items.

    Returns:
        array: array of items sorted in ascending order.

    Examples:
        >> bubble_sort([4, 7, 2, 6, 23, 5, 7])
        [2, 4, 5, 6, 7, 7, 23]

    """

    for i, next_i in enumerate(items): # enumerate through array of items
        try:
            if items[i+1] < next_i: # if next item is smaller than current item
                items[i] = items[i+1] # swap the two items
                items[i+1] = next_i
                bubble_sort(items)
        except IndexError: # if index out of bounds
            pass
    return items

def merge_sort(items):
    """

    Return array of items, sorted in ascending order using merge sort method.

    Args:
        items (array): list of array-like object of items.

    Returns:
        array: array of items sorted in ascending order.

    Examples:
        >> merge_sort([4, 7, 2, 5, 75, 2, 5])
        [2, 2, 4, 5, 5, 7, 75]

    """

    len_i = len(items)

    if len_i == 1: # end function
        return items

    mid_point = int(len_i / 2) # find midpoint

    i1 = merge_sort(items[:mid_point]) # divide list in halves
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2) # call helper function on each half

def merge(A, B):
    """

    Helper function for merge_sort() function.

    """
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list

def quick_sort(items):
    """

    Return array of items, sorted in ascending order using quick sort method.

    Args:
        items (array): list of array-like object of items.

    Returns:
        array: array of items sorted in ascending order.

    Examples:
        >> quicksort([3, 5, 2, 6, 4, 7, 4])
        [2, 3, 4, 4, 5, 6, 7]

    """

    high = []
    low = []
    pivot_list = []

    if len(items) <= 1: # end function if no items left
        return items
    else:
        pivot = items[0] # find first pivor point
        for i in items:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)
            else:
                pivot_list.append(i)
        high = quicksort(high)
        low = quicksort(low)

    return low + pivot_list + high
