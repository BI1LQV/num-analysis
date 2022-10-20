from functools import reduce
from sympy import symbols, integrate, poly, simplify
from numpy import arange
from matplotlib.pyplot import plot, show, legend
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

    units = list(map(Unit, range(0, n+1)))
    return poly(simplify(reduce(lambda sum, i: sum+i, units))).coeffs()


coff = fitting((1+t**2)**0.5, 0, 1, 1)

print(coff)


xs = arange(0, 1, 0.001)


def f1(x): return (1+x**2)**0.5


def f2(x):
    ret = 0
    for i in range(0, len(coff)):
        ret += coff[i]*x**(len(coff)-i-1)
    return ret


y1s = list(map(f1, xs))
y2s = list(map(f2, xs))

plot(xs, y1s)
plot(xs, y2s)
show()
