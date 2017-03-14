#ADDITIONAL FUNCION
def striplr(string, chars = None):
    return string.strip(chars).rstrip(chars)

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False