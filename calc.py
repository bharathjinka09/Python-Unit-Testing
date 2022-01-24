
def add(x, y):
    """Add Function"""
    if(type(x) not in [int,float] or type(y) not in [int,float]):
        raise ValueError("Value should be int or float")
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y