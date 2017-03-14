from tools.stringtools import striplr, is_int
from tools.othertools import euclid_gcd


class Fraction(object):

    def __init__(self, numerator=0, denominator=1, representation='default'):
        self.representation = representation
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
            if self.representation == 'f' or self.representation == 'float':
                return str(self.as_float())
            elif self.representation == 'd' or self.representation == 'default':
                return "{0}/{1}".format(self.numerator, self.denominator)
            elif self.representation == "b" or self.representation == "broken":
                factor = int(self.numerator)/int(self.denominator)
                if factor is not 0:
                    return str(factor) + ' {0}/{1}'.format(int(self.numerator)-factor*self.denominator, self.denominator)
                else:
                    return "{0}/{1}".format(self.numerator, self.denominator)
        else:
            return "{0}".format(self.numerator)


def read_fraction_from_string(string, representation='default'):
    cleaned_string = striplr(string)
    if is_int(cleaned_string):
        return Fraction(int(cleaned_string))
    else:
        parts = cleaned_string.split('/')
        return Fraction(int(parts[0]), int(parts[1]), representation)


