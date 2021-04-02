def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    min_val = a
    max_val = b
    step = c

    if step is None:
        step = 1
    if max_val is None:
        max_val = min_val
        min_val = 0
    current = min_val
    if (max_val > min_val and step > 0) or (max_val < min_val and step < 0):
        yield min_val
        while current < max_val - step:
            current += step
            yield current
    else:
        pass
