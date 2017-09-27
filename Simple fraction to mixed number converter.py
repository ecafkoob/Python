from fractions import Fraction


def mixed_fraction(s):
    l = [int(x) for x in s.split('/')]
    numer = Fraction(l[0], l[1]).numerator
    den = Fraction(l[0], l[1]).denominator
    if numer % den == 0:
        return str(int(numer / den))
    num = int(Fraction(numer, den) + 0.0)
    new_numer = abs(numer - (num) * den)
    if num == 0 and Fraction(l[0], l[1]) < 0:
        return '-'+str(new_numer) + '/' + str(den)
    elif num == 0 and Fraction(l[0], l[1]) > 0:
        return str(new_numer) + '/' + str(den)
    elif num != 0 and Fraction(l[0], l[1]) < 0:
        return str(num) + ' ' + str(new_numer) + '/' + str(den)
    elif num != 0 and Fraction(l[0], l[1]) > 0:
        return str(num) + ' ' + str(new_numer) + '/' + str(den)
