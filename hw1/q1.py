from numpy import exp
from matplotlib.pyplot import plot, show


def calcE(n): return (1+1/n)**n
def power10(k): return 10**k


x = range(1, 21)
listE = map(calcE, map(power10, x))
listDelta = map(lambda x: x-exp(1), listE)

plot(x, list(listDelta))
show()
