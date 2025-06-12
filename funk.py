import math as m

def funck(a, b):
    try:
        y = m.sqrt(((a+b)**3)/((a-b)**2))
    except ZeroDivisionError:
        result = 'there is zero divizion'
        raise ZeroDivisionError
    except ValueError:
        result = "can't divide zero without complex"
    except TypeError:
        result = 'this is not a number'
    else:
        result = round(y,4)
    return result