def sum_array(array):
    """

    Return sum of all items in array.

    Args:
        array (array): list or array-like object containing numerical values.

    Returns:
        int: sum of all items in array.

    Examples:
        >> sum_array([2, 5, 7, 3, 4])
        21

    """

    if len(array)==0: # if no numbers in input array
        return 0
    else:
        return array[0] + sum_array(array[1:]) #calculate sum recursively


def fibonacci(n):
    """

    Return nth term in fibonacci sequence.

    Args:
        n (int): number representing which term in fibonacci sequence to return.

    Returns:
        int: desired term in fibonaci sequence.

    Examples:
        >> fibonacci(16)
        987

    """

    if n <= 1: # if n too low to calculate neccessary fibonacci sequence further
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2)) # calculate fibonacci sequence recursively

def factorial(n):
    """

    Return n!

    Args:
        n (int): base factorial number.

    Returns:
        int: the factorial of n.

    Examples:
        >> factorial(5)
        120

    """

    if n <=1: # if n too low to calculate futher factorials
        return n
    else:
        return n * factorial(n-1) # calculate factorial of n recursively

def reverse(word):
    """

    Return word in reverse.

    Args:
        word (string): string value to be returned in reverse order.

    Returns:
        string: reverse of input word.

    Examples:
        >> reverse("hello world")
        "dlrow olleh"

    """

    if len(word) == 0: # if no letters left to be reversed
        return word
    else:
        return word[-1] + reverse(word[:-1]) # get last character en recursively get next characters
