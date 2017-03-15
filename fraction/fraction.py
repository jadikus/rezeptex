from tools.stringtools import striplr, is_int
from tools.othertools import euclid_gcd


class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("The denominator should be non-zero!")
        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator
        elif denominator < 0:
            numerator = -numerator
            denominator = -denominator

        factor = euclid_gcd(abs(numerator), abs(denominator))
        sign = numerator/abs(numerator)
        self.numerator = sign*numerator/factor
        self.denominator = denominator/factor

    def as_float(self):
        return float(self.numerator)/self.denominator

    def __add__(self, other):
        numerator = self.numerator*other.denominator + self.denominator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self._multiply(self, other)
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)

    def invert(self):
        return Fraction(self.denominator, self.numerator)

    def __div__(self, other):
        if isinstance(other, Fraction):
            return self * other.invert()
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)

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
        return "{0}/{1}".format(self.numerator, self.denominator)



def read_fraction_from_string(string):
    cleaned_string = striplr(string)
    if is_int(cleaned_string):
        return Fraction(int(cleaned_string))
    else:
        parts = cleaned_string.split('/')
        return Fraction(int(parts[0]), int(parts[1]))


def is_fraction(string):
    try:
        read_fraction_from_string(string)
        return True
    except ValueError:
        return False
