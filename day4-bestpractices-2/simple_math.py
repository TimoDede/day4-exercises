"""
A collection of simple math operations
"""

def simple_add(a,b):
    '''
    A function for adding a to b

    :param a: first value
    :param b: second value
    :return: Returns the sum
    '''
    return a+b

def simple_sub(a,b):
    """
    A function for subtracting b from a

    :param a: first value
    :param b: second value
    :return: Returns the difference
    """
    return a-b

def simple_mult(a,b):
    """
    A function for multiplying a and b

    :param a: first value
    :param b: second value
    :return: returns the product of the two numbers
    """
    return a*b

def simple_div(a,b):
    """
    A function for deviding a by b

    :param a: first value
    :param b: second value
    :return: Returns the quotient
    """
    return a/b

def poly_first(x, a0, a1):
    """
    A function for calculating the value of a first order polynom at given value x

    :param x: function value
    :param a0: 0th order term
    :param a1: 1st order term
    :return: Returns the value of a first order polynom
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    A function for calculating the value of a second order polynom at given value x

    :param x: function value
    :param a0: 0th order term
    :param a1: 1st order term
    :param a2: 2nd order term
    :return: Returns the value of a second order polynom
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
