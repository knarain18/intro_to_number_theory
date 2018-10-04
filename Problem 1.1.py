import math

def is_triangle(x):
    """
    This function tells you whether
    a number is a triangle number or not.
    By the definition in A Friendly
    Introduction to Number Theory by Silverman,
    a triangle number is a number that satisfies the equation
    n(n+1)/2 = p where n and p are positive, natural numbers.

    >>> is_triangle(3)
    True
    >>> is_triangle(11)
    False
    """
    n = (-1 + math.sqrt(1 + 8*x))/2
    return n*(n+1)/2 == x
