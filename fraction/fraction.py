from tools.stringtools import striplr, is_int
from tools.othertools import euklid_gcd


class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator
        elif denominator < 0:
            numerator = -numerator
            denominator = -denominator

        factor = euklid_gcd(abs(numerator), abs(denominator))
        sign = numerator/abs(numerator)
        self.numerator = sign*numerator/factor
        self.denominator = denominator/factor

    def as_float(self):
        return self.numerator/self.denominator

    def __add__(self, other):
        numerator = self.numerator*other.denominator + self.denominator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self._multiply(self, other)
        if isinstance(other, int):
            return Fraction(self.numerator*other, self.denominator)

    def invert(self):
        return Fraction(self.denominator, self.numerator)

    def __div__(self, other):
        if isinstance(other, Fraction):
            return self * other.invert()
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator*other)

    @staticmethod
    def _multiply(frac_a, frac_b):
        numerator = frac_a.numerator * frac_b.numerator
        denominator = frac_a.denominator * frac_b.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        return self + other.__negate()

    def __negate(self):
        return Fraction(-self.numerator, self.denominator)

    def __repr__(self):
        if self.denominator is not 1:
            return "{0}/{1}".format(self.numerator, self.denominator)
        else:
            return "{0}".format(self.numerator)


def read_fraction_from_string(string):
    cleaned_string = striplr(string)
    if is_int(cleaned_string):
        return Fraction(int(cleaned_string))

    try:
        cleaned_string.index('/')
        parts = cleaned_string.split('/')
        if is_int(parts[0]) and is_int(parts[1]):
            return Fraction(int(parts[0]), int(parts[1]))
    except ZeroDivisionError:
        print("The given denominator is zero. No Fraction is returned.")
        return None
    except ValueError:
        print("The given string couldn't be interpreted as a fraction.")
        return None

