def convertFracts(lst):
    fengmu = []
    sarr = []
    result = []
    for i in lst:
        fengmu.append(i[1])

    def gcd(a, b):
        if b == 0:
            return a

        return gcd(b, a % b)

    def lcm(c, d):
        return c * d / (gcd(c, d))

    sarr.append(lcm(fengmu[0], fengmu[1]))
    count = 0
    for i in fengmu[2:]:
        s = lcm(sarr[count], i)
        sarr.append(s)
        count += 1
    LCM = sarr[-1]

    def zoomUp(e, f, LCM):
        return [int(LCM / f * e), int(LCM)]

    for i in lst:
        result.append(zoomUp(i[0], i[1], LCM))
    return result


77033412951888085, 14949283383840498
'''
from fractions import gcd

def get_lcm(lst):
  return reduce(lambda x, y : x*y/gcd(x,y), lst)

def convertFracts(lst):
  lcm = get_lcm([ y for x, y in lst])
     return [ [x*lcm/y, lcm] for x, y in lst]
     
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b/gcd(a,b)
'''

