def make_capital(x):
    '''Capitalizes the first element in a string

    Args:
        x (str): a string to capitalize

    Returns:
        str (str): the arg string with the 1st element capitalized
    '''
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()
