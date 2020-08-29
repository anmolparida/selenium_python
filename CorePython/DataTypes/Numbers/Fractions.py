import fractions

print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1,3))
print(fractions.Fraction(0))
print(fractions.Fraction(1,-3))
print(fractions.Fraction(-1,3))
print(fractions.Fraction(-1,-3))

"""
While creating Fraction from float, we might get some unusual results. T
his is due to the imperfect binary floating point number representation as seen in decimals.
Fortunately, Fraction allows us to instantiate with string as well. This is the preferred option when using decimal numbers
"""

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

from fractions import Fraction as F

print(F(1, 3) + F(1, 3))
print(1 / F(5, 6))
print(F(-3, 10) > 0)
print(F(-3, 10) < 0)