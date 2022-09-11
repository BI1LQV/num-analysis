from q3_1 import EPISODE1, EPISODE2, START_AT


def f(x): return x**2-3*x+2
def fPrime(x): return 2*x-3


def newtonIter(f, fPrime, x):
    xk = x-f(x)/fPrime(x)
    if abs(f(x)) > EPISODE1 or abs(x-xk) > EPISODE2:
        return newtonIter(f, fPrime, xk)
    return xk


def assess(start):
    try:
        return newtonIter(f, fPrime, start)
    except:
        return "not pass"


print(assess(START_AT))
