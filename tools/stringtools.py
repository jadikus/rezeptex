#ADDITIONAL FUNCION




def striplr(string, chars = None):
    return string.strip(chars).rstrip(chars)

def is_int(string):
    try:
        int(string)
        return True
    except ValueError, TypeError:
        return False

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def make_quantity(string):
    """
    function to make a Quantity
    :param string:
    :return:
    """
    pass