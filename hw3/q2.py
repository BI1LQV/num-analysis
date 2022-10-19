from functools import reduce
from sympy import symbols, integrate, poly

t = symbols('t')
LEGEND_MAP = {
    0: 1+0*t,
    1: t
}


def getLegend(k):
    ret = LEGEND_MAP.get(k)
    if ret:
        return ret
    ret = (2*k+1)/(k+1)*t*getLegend(k-1) - k/(k+1)*getLegend(k-2)
    LEGEND_MAP[k] = ret
    return ret


def fitting(f, a, b, n):
    transform = (2*t-(a+b))/(b-a)

    def Unit(i):
        led = getLegend(i).subs(t, transform)
        return float(integrate(
            led*f, (t, a, b)
        )/integrate(
            led*led, (t, a, b)
        ))*led

    units = list(map(Unit, range(0, n)))
    return poly(reduce(lambda sum, i: sum+i, units)).coeffs()


print(fitting((1+t**2)**0.5, 0, 1, 2))
